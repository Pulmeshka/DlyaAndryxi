from aiogram import types
from ..db import db, pets
from random import randint
from .confog import *

randomButton = types.InlineKeyboardMarkup(row_width=2)
randomButton1 = types.InlineKeyboardButton(text='чёт✅', callback_data='randomOne')
randomButton2 = types.InlineKeyboardButton(text='не чёт❌', callback_data='randomTwo')
randomButton.add(randomButton1, randomButton2)

async def viper(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    if await db.vip(user_id) == 1:
        try:
            suma = message.text.split()[1]
            try:
                suma = int(suma)
                coin = await db.get_coin(user_id)
                coin = int(coin)
                if coin < suma or suma < 1:
                    await message.answer('недостаточно монет❌')
                    return
                coin -= suma
                await db.update_coin(user_id, coin)
                await message.reply('чёт или не чёт', reply_markup=randomButton)
                
            except ValueError:
                await message.answer('ставка должна быть числом❌')
        except IndexError:
            await message.answer('а ставка где❓')
    else:
        await message.answer('у тебя нету VIP❌')


async def viper_random1(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    randomizer = randint(1, 6)
    wearpet = await pets.get_wearpet(user_id)
    plus_sum = 1
    if wearpet in x1:
        plus_sum = 2
    elif wearpet in x2:
        plus_sum = 3
    elif wearpet in x3:
        plus_sum = 4
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        if randomizer == 2 or randomizer == 4 or randomizer == 6:
            suma = call.message.text.split()[1]
            coin = await db.get_coin(user_id)
            await call.message.edit_text(f'вы победили, ставка увеличена🎉\nчисло: {randomizer}')
            suma = int(suma)
            coin = int(coin)
            suma *= plus_sum
            coin += suma
            await db.update_coin(user_id, coin)
        else:
            await call.message.edit_text(f'вы проиграли, ставка потеряна🙄\nчисло: {randomizer}')

async def viper_random2(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    randomizer = randint(1, 6)
    wearpet = await pets.get_wearpet(user_id)
    plus_sum = 1
    if wearpet in x1:
        plus_sum = 2
    elif wearpet in x2:
        plus_sum = 3
    elif wearpet in x3:
        plus_sum = 4
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        if randomizer == 1 or randomizer == 3 or randomizer == 5:
            suma = call.message.text.split()[1]
            coin = await db.get_coin(user_id)
            await call.message.edit_text(f'вы победили, ставка увеличена🎉\nчисло: {randomizer}')
            suma = int(suma)
            coin = int(coin)
            suma *= plus_sum
            coin += suma
            await db.update_coin(user_id, coin)
        else:
            await call.message.edit_text(f'вы проиграли, ставка потеряна🙄\nчисло: {randomizer}')