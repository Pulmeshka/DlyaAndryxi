from aiogram import types
from db import db
from main import dp
from .LISTS import *

@dp.message_handler(commands=['profile'])
async def balane_command(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    coin = await db.get_balance(user_id)
    diamond = await db.get_diamond(user_id)
    skin = await db.get_skin(user_id)
    await message.answer_sticker(f'{skins_list[skin]}')
    await message.answer(f"Профиль игрока <b>{name}</b>\n➡️коины🪙: <b>{coin}</b>\n➡️алмазы💎: <b>{diamond}</b>\n➡️скин🦁: <b>{skinName_list[skin]}</b>\n➡️ID - <code>{user_id}</code>", parse_mode='HTML')  



@dp.message_handler(commands=['click'])
async def click_command(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if user_id in admin_list:
        coin = await db.get_balance(user_id)
        coin = coin + 10_000
        await db.update_balance(user_id, coin)
        await message.answer(f'на ваш баланс поступил 10.000 коин✅\nновый баланс🪙: {coin}')
    else:
        await message.answer(f'отказано в доступе❌\nПричина: <b>вы не являетесь админом бота</b>', parse_mode='HTML')