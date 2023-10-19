from aiogram import types
from ..db import db, pets
from .confog import dp

async def gift_vip_command(message: types.Message):  
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
    vip1 = await db.vip(user_id)
    vip2 = await db.vip(player_id)
    if vip1 == 0:
        await message.answer('У тебя нету VIP❌')
        return
    if vip2 == 1:
        await message.answer(f'<b>{name2}</b> уже имеет вип❌', parse_mode='HTML')
        return
    diamond = await db.get_diamond(user_id)
    diamond = int(diamond)
    if diamond < 450:
        await message.answer('недостаточно средств❌')
        return
    
    coin = await db.get_coin(player_id)
    coin = int(coin)
    vip2 = 1
    diamond -= 450
    coin += 5000
    pet_vip = 1
    await db.up_vip(player_id, vip2)
    await db.update_diamond(user_id, diamond)
    await db.update_coin(player_id, coin)
    await pets.update_vip(player_id, pet_vip)
    await message.answer_sticker(f'CAACAgIAAxkBAQPuQ2UkQsEaNwaJ0vwlCpriSTUVVFI_AAJWAQACFkJrCnHAhwVgxqSFMAQ')
    await message.answer(f'🥳<b>{name}</b> ПРИОБРЁЛ <b>VIP</b> ДЛЯ <b>{name2}</b>🥂', parse_mode='HTML')

async def gift_premium_egg_command(message: types.Message):  
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
    vip1 = await db.vip(user_id)
    if vip1 == 0:
        await message.answer('У тебя нету VIP❌')
        return
    diamond = await db.get_diamond(user_id)
    diamond = int(diamond)
    if diamond < 100:
        await message.answer('недостаточно средств❌')
        return
    
    egg = await pets.premium(player_id)
    egg += 1
    diamond -= 100
    await pets.premium_up(player_id, egg)
    await db.update_diamond(user_id, diamond)
    await message.answer_sticker(f'CAACAgIAAxkBAQPuQ2UkQsEaNwaJ0vwlCpriSTUVVFI_AAJWAQACFkJrCnHAhwVgxqSFMAQ')
    await message.answer(f'🥳<b>{name}</b> ПРИОБРЁЛ <b>POKEMON EGG✨</b> ДЛЯ <b>{name2}</b>🥂', parse_mode='HTML')