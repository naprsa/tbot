from aiogram import Dispatcher
from .throttling import ThrottlingMiddleware
from .database import GetDBUser


def setup(dp: Dispatcher):
    dp.setup_middleware(ThrottlingMiddleware())
    dp.setup_middleware(GetDBUser())
