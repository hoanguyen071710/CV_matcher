from enum import Enum

from ...db.PostgresConnection import PostgresConnection
from ...model.dao.ExtractConfigDAO import ExtractConfigDAO
from ...utils import Utils

class ConfigService:
    def __init__(self, config: dict):
        self.conn = PostgresConnection("localhost", 54320, "postgres", "postgres", "postgres")
        self.configDao = ExtractConfigDAO(self.conn)
        self.config = Utils.dict_to_model(config, "ExtractConfig")

    def insert_config(self):
        self.configDao.insert([self.config])
        