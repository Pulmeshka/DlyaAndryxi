from aiogram import types
from ..db import db

async def updates_command(message: types.Message): 
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await message.answer(
        'свежих обновлений нету'
        )