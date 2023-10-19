from aiogram import types
from ..db import db, pets
from .confog import dp, wear_pet
from random import randint


eggOpenButton1 = types.InlineKeyboardButton(text='обычное яйцо🥚', callback_data='DefEgg')
eggOpenButton2 = types.InlineKeyboardButton(text='покемон яйцо✨', callback_data='PremEgg')

async def open_egg(message: types.Message):
    eggOpenButton = types.InlineKeyboardMarkup()   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    if await pets.default(user_id) > 0:
        eggOpenButton.add(eggOpenButton1)
    if await pets.premium(user_id) > 0:
        eggOpenButton.add(eggOpenButton2)
    await message.reply('какое яйцо хотите открыть', reply_markup=eggOpenButton)

async def OpenDefEgg(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    egg = await pets.default(user_id)
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        if egg > 0:
            random_rare = randint(1, 4)
            if random_rare == 1:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил батерфри')
                pet = await pets.butterfly(user_id)
                pet += 1
                egg -= 1
                await pets.update_butterfly(user_id, pet)
                await pets.default_up(user_id, egg)
            elif random_rare == 2:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил собаку')
                pet = await pets.dog(user_id)
                pet += 1
                egg -= 1
                await pets.update_dog(user_id, pet)
                await pets.default_up(user_id, egg)
            elif random_rare == 3:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил свинью')
                pet = await pets.pig(user_id)
                pet += 1
                egg -= 1
                await pets.update_pig(user_id, pet)
                await pets.default_up(user_id, egg)
            elif random_rare == 4:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил корову')
                pet = await pets.cow(user_id)
                pet += 1
                egg -= 1
                await pets.update_cow(user_id, pet)
                await pets.default_up(user_id, egg)
        else:
            await call.message.delete()

async def OpenPremEgg(call: types.CallbackQuery):#
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    egg = await pets.premium(user_id)#
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        if egg > 0:
            random_rare = randint(1, 100)
            if random_rare > 0 and random_rare < 31:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил лугия')
                pet = await pets.lugia(user_id)
                pet += 1
                egg -= 1
                await pets.update_lugia(user_id, pet)
                await pets.premium_up(user_id, egg)
            elif random_rare > 30 and random_rare < 61:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил бульбозавра')
                pet = await pets.bulbos(user_id)
                pet += 1
                egg -= 1
                await pets.update_bulbos(user_id, pet)
                await pets.premium_up(user_id, egg)
            elif random_rare > 60 and random_rare < 91:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил тортанка')
                pet = await pets.tortank(user_id)
                pet += 1
                egg -= 1
                await pets.update_tortank(user_id, pet)
                await pets.premium_up(user_id, egg)
            elif random_rare > 90 and random_rare < 101:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил сквиртла')
                pet = await pets.skwirt(user_id)
                pet += 1
                egg -= 1
                await pets.update_skwirtl(user_id, pet)
                await pets.premium_up(user_id, egg)
        else:
            await call.message.delete()