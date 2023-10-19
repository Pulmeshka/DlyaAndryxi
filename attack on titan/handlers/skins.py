from aiogram import types
from db import db
from main import dp
from .LISTS import *

@dp.message_handler(commands=['allSkins'])
async def skins_command(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    await message.answer(f'всего скинов в игре: <b>{skin_all}</b>\nчтобы посмотреть инфу про скин напишите <code>/skininfo 1</code>', parse_mode='HTML')

@dp.message_handler(commands=['skininfo'])
async def skininfo_command(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if  len(message.text.split()) < 2:
        await message.answer('❌вы не указали номер скина❌')
        return
    skin_num = message.text.split()[1]
    try:
        skin_num = int(skin_num)
        if skin_num > skin_all:
            await message.answer(f'❌в боте всего скинов <b>{skin_all}</b>❌', parse_mode='HTML')
            return
        await message.answer_sticker(f'{skins_list[skin_num]}')
        await message.answer(f'название❤️: <b>{skinName_list[skin_num]}</b>', parse_mode='HTML')
    except ValueError:
        await message.answer('❌номер скина должен быть числом❌')