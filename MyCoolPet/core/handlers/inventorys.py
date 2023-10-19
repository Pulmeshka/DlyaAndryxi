from aiogram import types
from ..db import db
from .confog import dp

async def inventory(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    glove = await db.get_glove(user_id)
    await message.reply(
        '<b>↷ваш инвентарь↶</b>\n'
        f'перчатка🧤 - {glove}%'
    , parse_mode='HTML')