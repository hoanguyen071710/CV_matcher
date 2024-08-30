from typing import List, Union, Dict

from sqlalchemy.orm import Session
from sqlalchemy import select, delete, insert, update

from .DAO import DAO
from ..entities.Job import Job
from ..entities.ExtractConfig import ExtractConfig


class ExtractConfigDAO(DAO):

    def __init__(self, connector):
        self.__engine = connector.getEngine()

    def insert(self, t: ExtractConfig) -> None:
        with Session(self.__engine) as session:
            with session.begin():
                session.add(t)

    def insert_all(self, t: Union[List[ExtractConfig], List[Dict]]) -> None:
        with Session(self.__engine) as session:
            with session.begin():
                if (len(list) != 0) and isinstance(t[0], Job):
                    session.add_all(t)
                if (len(list) != 0) and isinstance(t[0], dict):
                    session.execute(
                        insert(ExtractConfig),
                        t
                    )

    def get_all(self) -> List[ExtractConfig]:
        with Session(self.__engine) as session:
            statement = select(ExtractConfig)
            return session.execute(statement).all()

    def delete_all(self):
        with Session(self.__engine) as session:
            with session.begin():
                session.query(ExtractConfig).delete()
                session.commit()

    def delete(self, id: str):
        with Session(self.__engine) as session:
            with session.begin():
                session.query(ExtractConfig).filter(ExtractConfig.id == id).delete()
                session.commit()

    def update(self, t: ExtractConfig):
        with Session(self.__engine) as session:
            with session.begin():
                session.execute(
                    update(ExtractConfig)
                    .where(ExtractConfig.id == t.id)
                    .values(t.all_key_values(exclude_primary_key=True))
                )
