from aiogram import types
from ..db import db

async def obnyt(message: types.Message): 
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if not message.reply_to_message:
        await message.answer('нужно ответить на сообщение')
        return
    await message.answer_sticker('CAACAgIAAxkBAAEIEHZkCebPmhWV7p8LbSWrRIpjT1r0TgAC_SsAAtIhCEg7Lm89KBucdS8E')
    await message.answer(f'<b>{name}</b> обнял🤗 <b>{message.reply_to_message.from_user.first_name}</b>', parse_mode='HTML')

async def ydarit(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if not message.reply_to_message:
        await message.answer('нужно ответить на сообщение')
        return
    await message.answer_sticker('CAACAgIAAxkBAAEIEIJkCepmtHUZpYPxVR2xluBJQhrGGQACqSoAAlXLCUiIAbdnbua9JC8E')
    await message.answer(f'<b>{name}</b> ударил👊 <b>{message.reply_to_message.from_user.first_name}</b>', parse_mode='HTML')

async def poselovat(message: types.Message): 
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if not message.reply_to_message:
        await message.answer('нужно ответить на сообщение')
        return
    await message.answer_sticker('CAACAgIAAxkBAAEIEI5kCeszqrB5npsjmroMhbu1V3qnKQACMSEAApgtuUv_AgMFl8qeSi8E')
    await message.answer(f'<b>{name}</b> поцеловал💖 <b>{message.reply_to_message.from_user.first_name}</b>', parse_mode='HTML')

async def napast(message: types.Message): 
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if not message.reply_to_message:
        await message.answer('нужно ответить на сообщение')
        return
    await message.answer_sticker('CAACAgIAAxkBAAEIEJBkCetlP0ogDxa3dLyuS0yPyvYKCQACjiUAAjN-CEgyB_50alY8Sy8E')
    await message.answer(f'<b>{name}</b> напал на😈 <b>{message.reply_to_message.from_user.first_name}</b>', parse_mode='HTML')

async def poglidit(message: types.Message): 
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if not message.reply_to_message:
        await message.answer('нужно ответить на сообщение')
        return
    await message.answer_sticker('CAACAgIAAxkBAAGoxrdkExCsm1wS2sSku77jy6N88Jj1OgACdBYAAj-pSEh0vElOfonYLi8E')
    await message.answer(f'<b>{name}</b> погладил💕 <b>{message.reply_to_message.from_user.first_name}</b>', parse_mode='HTML')

async def vipit(message: types.Message): 
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if not message.reply_to_message:
        await message.answer('нужно ответить на сообщение')
        return
    await message.answer_sticker('CAACAgIAAxkBAAGoxt5kExFzGaiE-_UV3OaKc8HwBDch3gACzwEAAladvQrnnqjJFNimhS8E')
    await message.answer(f'<b>{name}</b> бухнул🍻 с <b>{message.reply_to_message.from_user.first_name}</b>', parse_mode='HTML')

async def vikinyt(message: types.Message): 
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if not message.reply_to_message:
        await message.answer('нужно ответить на сообщение')
        return
    if await db.vip(user_id) == 1:
        await message.answer_sticker('CAACAgIAAxkBAQPrvWUkOSjgVeRfcm2D7y13s-LGi6JrAAJ-AwACbbBCA3EZlrX3Vpb0MAQ')
        await message.answer(f'<b>{name}</b> выкинул как мусор игрока🗑️ <b>{message.reply_to_message.from_user.first_name}</b>', parse_mode='HTML')
    else:
        return