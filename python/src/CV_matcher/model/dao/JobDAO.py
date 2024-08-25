from typing import List, Union, Dict

from sqlalchemy.orm import Session
from sqlalchemy import select, delete, insert, update

from .DAO import DAO
from ..entities.Job import Job


class JobDAO(DAO):

    def __init__(self, connector):
        self.__engine = connector.getEngine()

    def insert(self, t: Job) -> None:
        with Session(self.__engine) as session:
            with session.begin():
                session.add(t)

    def insert_all(self, t: Union[List[Job], List[Dict]]) -> None:
        with Session(self.__engine) as session:
            with session.begin():
                if (len(list) != 0) and isinstance(t[0], Job):
                    session.add_all(t)
                if (len(list) != 0) and isinstance(t[0], dict):
                    session.execute(
                        insert(Job),
                        t
                    )

    def get_all(self) -> List[Job]:
        with Session(self.__engine) as session:
            statement = select(Job)
            return session.execute(statement).all()

    def delete_all(self):
        with Session(self.__engine) as session:
            with session.begin():
                session.query(Job).delete()
                session.commit()

    def delete(self, id: str):
        with Session(self.__engine) as session:
            with session.begin():
                session.query(Job).filter(Job.id == id).delete()
                session.commit()

    def update(self, t):
        with Session(self.__engine) as session:
            with session.begin():
                session.execute(
                    update(Job)
                    .where(Job.id == t.id)
                    .values(t.all_key_values(exclude_primary_key=True))
                )
