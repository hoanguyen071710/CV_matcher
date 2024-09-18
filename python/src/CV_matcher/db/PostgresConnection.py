import psycopg2
from sqlalchemy import create_engine

from .Connection import Connection


class PostgresConnection(Connection):
    def __init__(self, host, port, user, password, database):
        # self.__host = host
        # self.__port = port
        # self.__user = user
        # self.__password = password
        # self.__database = database
        self.__connString = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
        self.__engine = create_engine(self.__connString, echo=True)

    def getEngine(self):
        return self.__engine
    