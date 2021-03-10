from sqlalchemy import BigInteger, String
from sqlalchemy import Column
from sqlalchemy import sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(128))

    query: sql.Select
