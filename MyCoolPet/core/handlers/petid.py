from aiogram import types
from ..db import db
from .confog import *


async def check_pet_id(message: types.Message):  
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    try:     
        id = message.text.split()[1]
        try:
            id = int(id)
            if id > pets_all or id < 1:
                await message.answer('такого ID не существует❌')
                return
            await message.answer_sticker(f'{wear_pet[id]}')
            if id in exclusive_id:
                text = '🎗️ексклюзивный питомец🎗️'
            elif id in common:
                text = '🗽обычный питомец🗽'
            elif id in rare:
                text = '⭕редкий питомец⭕'
            elif id in legendary:
                text = '💢легендарный питомец💢'
            elif id in mystic:
                text = '💫мистический питомец💫'

            if id in x1:
                xx = 'x1'
            elif id in x2:
                xx = 'x2'
            elif id in x3:
                xx = 'x3'

            await message.answer(f'Питомец🐶: <b>{rare_pet[id]}{pets_id[id]}{rare_pet[id]}</b>\n{text}\nумножитель: {xx}', parse_mode='HTML')
        except ValueError:
            await message.answer('ID питомца должен быть числом❌')
    except IndexError:
        await message.answer('ты не ввел ID❌')