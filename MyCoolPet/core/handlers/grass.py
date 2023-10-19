from aiogram import types
from ..db import db, pets
from random import randint
from .confog import *

grassButton = types.InlineKeyboardMarkup(row_width=2)
grassButton1 = types.InlineKeyboardButton(text='🌿', callback_data='grassOne')
grassButton2 = types.InlineKeyboardButton(text='🌿', callback_data='grassTwo')
grassButton.add(grassButton1, grassButton2)

async def grass_game(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
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
            await message.reply(f'ставка: {suma}\nвыбери травку\nпомощь по игре - /helpgrass', reply_markup=grassButton)
        except ValueError:
            await message.answer('ставка должна быть числом❌')
    except IndexError:
        await message.answer('а ставка где❓')

async def Grass_random(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    radnom_grass = randint(1, 2)
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
        if radnom_grass == 1:
            suma = call.message.text.split()[1]
            coin = await db.get_coin(user_id)
            await call.message.edit_text('вы победили, ставка увеличена🎉')
            suma = int(suma)
            coin = int(coin)
            suma *= plus_sum
            coin += suma
            await db.update_coin(user_id, coin)
        else:
            await call.message.edit_text('вы проиграли, ставка потеряна🙄')

async def Grass_random2(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    radnom_grass = randint(1, 2)
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
        if radnom_grass == 2:
            suma = call.message.text.split()[1]
            coin = await db.get_coin(user_id)
            await call.message.edit_text('вы победили, ставка увеличена🎉')
            suma = int(suma)
            coin = int(coin)
            suma *= plus_sum
            coin += suma
            await db.update_coin(user_id, coin)
        else:
            await call.message.edit_text('вы проиграли, ставка потеряна🙄')


async def grass_help(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    await message.answer(
        'помощь по игре "травка"😍\n'
        'в начале выдолжны прописать "травка <ставка>"\n'
        'после чего вы увидете сообщение с кнопками\n'
        'в одной из кнопок лежат монетки которые вы потеряли, так ещё и подарочек в виде увеличение этих монет\n'
        'если вы выберете правильную травку, вы заберете эти монеты\n'
        'если нет - увы, лис своровал ваши монеты')