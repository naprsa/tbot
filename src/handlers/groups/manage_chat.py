import asyncio
import datetime
import re

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.exceptions import BadRequest

from src.filters import IsGroup, AdminFilter
from src.loader import dp, bot


@dp.message_handler(IsGroup(), Command("ro", prefixes="!/"), AdminFilter())
async def set_readonly_mode(msg: types.Message):
    member = msg.reply_to_message.from_user
    member_id = member.id
    chat_id = msg.chat.id
    command_parse = re.compile(r"(!ro|/ro) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(msg.text)
    time = parsed.group(2)
    comment = parsed.group(3)
    if not time:
        time = 5
    else:
        time = int(time)
    until_date = datetime.datetime.now() + datetime.timedelta(minutes=time)

    ReadOnlyPermissions = types.ChatPermissions(
        can_send_messages=False,
        can_send_polls=False,
        can_change_info=False,
        can_invite_users=True,
        can_send_media_messages=False,
        can_send_other_messages=False,
        can_pin_messages=False,
        can_add_web_page_previews=False,
    )
    try:
        await bot.restrict_chat_member(
            chat_id,
            user_id=member_id,
            permissions=ReadOnlyPermissions,
            until_date=until_date,
        )
        service_msg = await msg.answer(
            f"Пользователь {member.get_mention()} замучен на {time} минут, по причине {comment}"
        )
    except BadRequest:
        service_msg = await msg.answer(
            "Пользователь является администратором - отклонено!"
        )

    await asyncio.sleep(5)
    await service_msg.delete()


@dp.message_handler(IsGroup(), Command("ro", prefixes="!/"), AdminFilter())
async def set_readonly_mode(msg: types.Message):
    member = msg.reply_to_message.from_user
    member_id = member.id
    chat_id = msg.chat.id

    AllowedPermissions = types.ChatPermissions(
        can_send_messages=True,
        can_send_polls=True,
        can_change_info=False,
        can_invite_users=True,
        can_send_media_messages=True,
        can_send_other_messages=True,
        can_pin_messages=False,
        can_add_web_page_previews=True,
    )
    await msg.chat.restrict(
        user_id=member_id, permissions=AllowedPermissions, until_date=0
    )
    await msg.reply(f"Пользователь {member.full_name} был разбанен!")
