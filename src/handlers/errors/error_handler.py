from loguru import logger
from aiogram.types import Update
from src.loader import dp


@dp.errors_handlers()
async def errors_handler(update: Update, exception):
    """
    Exception handler. Catches all exceptions within task factory tasks.
    :param dispatcher:
    :param update:
    :param exception:
    :return: stdout logging
    """
    from aiogram.utils.exceptions import (
        Unauthorized,
        InvalidQueryID,
        TelegramAPIError,
        CantDemoteChatCreator,
        MessageNotModified,
        MessageToDeleteNotFound,
        MessageTextIsEmpty,
        RetryAfter,
        CantParseEntities,
        MessageCantBeDeleted,
        BadRequest,
    )

    if isinstance(exception, CantDemoteChatCreator):
        logger.debug(f"Can't demote chat creator. {exception}")
        return True

    if isinstance(exception, MessageNotModified):
        logger.debug(f"Message not modified. {exception}")
        return True

    if isinstance(exception, MessageCantBeDeleted):
        logger.debug(f"Message can't be deleted. {exception}")
        return True

    if isinstance(exception, MessageToDeleteNotFound):
        logger.debug(f"Message to delete not found. {exception}")
        return True

    if isinstance(exception, MessageTextIsEmpty):
        logger.debug(f"Message text is empty. {exception}")
        return True

    if isinstance(exception, Unauthorized):
        logger.debug(f"Unauthorized: {exception}")
        return True

    if isinstance(exception, InvalidQueryID):
        logger.debug(f"InvalidQueryID: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, TelegramAPIError):
        logger.debug(f"TelegramAPIError: {exception}")
        return True

    if isinstance(exception, RetryAfter):
        logger.debug(f"RetryAfter: {exception}")
        return True

    if isinstance(exception, CantParseEntities):
        logger.debug(f"CantParseEntities: {exception} \nUpdate: {update}")
        return True

    if isinstance(exception, BadRequest):
        logger.debug(f"BadRequest: {exception} \nUpdate: {update}")
        return True
