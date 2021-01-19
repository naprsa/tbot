from aiogram import Dispatcher

from .admins import AdminFilter
from .is_private import IsPrivate


def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPrivate)
