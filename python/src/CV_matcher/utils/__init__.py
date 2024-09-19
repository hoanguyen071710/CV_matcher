from sqlalchemy.dialects.postgresql.base import PGInspector
from typing import Dict, List, Any
import hashlib

from ..model.entities.ExtractConfig import ExtractConfig
from ..model.entities.Jobs import Jobs


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

    @staticmethod
    def deserialize_model(model: object) -> Dict[str, Any]:
        return {k:v for k, v in model.__dict__.items() if k != '_sa_instance_state'}
    
    @staticmethod
    def hash_model_values(model: object) -> str:
        valListStr = [str(v).lower() for k, v in Utils.deserialize_model(model).items() if k != 'id']
        valStrEncoded = "_".join(valListStr).encode("utf-8")
        return hashlib.sha256(valStrEncoded).hexdigest()
    
    @staticmethod
    def dict_to_model(dict_val: Dict[str, Any], model_name: str) -> ExtractConfig:
        if model_name == "ExtractConfig":
            return ExtractConfig(**dict_val)
        if model_name == "Jobs":
            return Jobs(**dict_val)