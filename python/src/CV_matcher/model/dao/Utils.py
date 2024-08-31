from enum import Enum
from psycopg2 import sql
from sqlalchemy import inspect
from sqlalchemy.dialects.postgresql.base import PGInspector


# class DatabaseType(Enum):
#     POSTGRESQL = {
#         "check_if_table_exists": """
#             SELECT EXISTS (
#                 SELECT FROM information_schema.tables 
#                 WHERE    table_name   = {}
#             );
#         """
#     }

class Utils:

    @staticmethod
    def check_if_table_exists(conn: any, table_name: str, schema: str) -> bool:
        engine = conn.getEngine()
        print("Checking if table {}.{} exists".format(schema, table_name))
        insp = PGInspector(bind=engine)
        return insp.has_table(
            table_name=table_name,
            schema=schema
        )

    @staticmethod
    def create_table(conn: any, table_name: str, model: any):
        engine = conn.getEngine()
        if not Utils.check_if_table_exists(conn, table_name):
            engine = conn.getEngine()
            model.__table__.create(engine)
            print("Table {} created".format(table_name))
            return False
        else:
            print("Table {} already exists".format(table_name))
            return True
