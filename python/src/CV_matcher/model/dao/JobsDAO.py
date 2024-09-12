from typing import List, Union, Dict
from sqlalchemy.orm import Session
from sqlalchemy import select, delete, insert, update
from sqlalchemy.dialects import postgresql as pg

from .DAO import DAO
from ..entities.Jobs import Jobs
from ...utils import Utils


class JobsDAO(DAO):

    def __init__(self, connector):
        self._engine = connector.getEngine()

    def insert(self, t: List[Jobs]) -> None:
        """
        Insert into database
        Note: 
            Inserting also handles create hash key for records, based on concatenation of fields
            This is to avoid duplicated records in the database, by implementing on_conflict_do_nothing on the hash key
        :param t: list of ExtractConfig
        :return: None
        """
        valList = []
        for rec in t:
            # rec.id = Utils.hash_model_values(rec)
            valList.append(Utils.deserialize_model(rec))
        with Session(self._engine) as session:
            with session.begin():
                session.execute(
                    pg.insert(Jobs).values(valList).on_conflict_do_nothing()
                )

    def get_by_id(self, id: Union[str, int]) -> Jobs:
        with Session(self._engine) as session:
            statement = select(Jobs).where(Jobs.id == id)
            return session.execute(statement).first()
        
    def get_all(self) -> List[Jobs]:
        with Session(self._engine) as session:
            statement = select(Jobs)
            return session.execute(statement).all()

    def delete_all(self):
        with Session(self._engine) as session:
            with session.begin():
                session.query(Jobs).delete()
                session.commit()

    def delete(self, id: str):
        with Session(self._engine) as session:
            with session.begin():
                session.query(Jobs).filter(Jobs.id == id).delete()
                session.commit()

    def update(self, t: Jobs):
        with Session(self._engine) as session:
            with session.begin():
                session.execute(
                    update(Jobs)
                    .where(Jobs.id == t.id)
                    .values(Utils.deserialize_model(t))
                )
