from enum import Enum
from psycopg2 import sql
from sqlalchemy import inspect


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
    def check_if_table_exists(conn: any, table_name: str) -> bool:
        engine = conn.getEngine()
        insp = inspect(engine)
        return insp.has_table(table_name)

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
