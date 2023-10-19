from aiogram import types
from ..db import db, pets
from .confog import dp


async def pay_coin(message: types.Message):  
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    if not message.reply_to_message:
        await message.answer('ты не ответил на сообщение')
        return
    player_id = message.reply_to_message.from_user.id
    name2 = message.reply_to_message.from_user.full_name
    user2 = message.reply_to_message.from_user.username
    await db.insert_user(player_id, name2, user2)
    if await db.get_ban(player_id) == 1:
        await message.answer('бедным нужнее, не то что забаненым')
        return
    if message.reply_to_message.from_user.is_bot:
        await message.answer('❌')
        return
    if player_id == user_id:
        await message.answer('а ловко ты это придумал')
        return
    try:     
        suma = message.text.split()[1]
        try:
            suma = int(suma)
            coin = await db.get_coin(user_id)
            player_coin = await db.get_coin(player_id)
            coin = int(coin)
            player_coin = int(player_coin)
            if suma > coin:
                await message.answer('недостаточно денег❌')
                return
            coin -= suma
            player_coin += suma
            await db.update_coin(user_id, coin)
            await db.update_coin(player_id, player_coin)
            await message.reply(f'<b>{name2}</b> получил <b>{suma}</b> монет от <b>{name}</b>', parse_mode='HTML')
        except ValueError:
            await message.answer('сума должна быть числом')
    except IndexError:
        await message.answer('ты не ввел суму')
        