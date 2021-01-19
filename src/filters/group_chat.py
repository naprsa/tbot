from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsGroup(BoundFilter):
    async def check(selfself, msg: types.Message) -> bool:
        return msg.chat.type in (types.ChatType.GROUP, types.ChatType.SUPER_GROUP)
