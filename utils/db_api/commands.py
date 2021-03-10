from sqlalchemy.testing import db

from utils.db_api.shemas.user import User
from utils.db_api.shemas.items import Item
from asyncpg import UniqueViolationError
from gino.exceptions import NoResultFound
from random import choice


async def add_user(id: int, name: str):
    try:
        user = User(id=id, name=name, is_registered=True)
        await user.create()
    except UniqueViolationError:
        pass


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def select_user(id: int):
    user = await User.query.where(User.id == id).gino.one()
    return user


async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total
