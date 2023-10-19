from aiogram import types
from ..db import db, pets
from .confog import dp

#ДОБАВИТЬ ТУТ
goldpet1 = types.InlineKeyboardButton(text='батерфри🦋', callback_data='go1')
goldpet2 = types.InlineKeyboardButton(text='собака🐶', callback_data='go2')
goldpet3 = types.InlineKeyboardButton(text='свинья🐷', callback_data='go3')
goldpet4 = types.InlineKeyboardButton(text='корова🐮', callback_data='go4')

#ДОБАВИТЬ ТУТ
async def gold_pet_comamnd(message: types.Message):   
    goldpetButton = types.InlineKeyboardMarkup(row_width=2)
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    if await pets.butterfly(user_id) > 7:
        goldpetButton.add(goldpet1)
    if await pets.dog(user_id) > 7:
        goldpetButton.add(goldpet2)
    if await pets.pig(user_id) > 7:
        goldpetButton.add(goldpet3)
    if await pets.cow(user_id) > 7:
        goldpetButton.add(goldpet4)

    await message.reply('какого питомца желаешь скрестить', reply_markup=goldpetButton)

async def GOLDbutterfly(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    pet = await pets.butterfly(user_id)
    gold = await pets.butterflyG(user_id)
    pet = int(pet)
    gold = int(gold)
    wearpet = await pets.get_wearpet(user_id)
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        if pet > 7:
            if wearpet != 1:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил ✨батерфри🦋✨')
                pet -= 8
                gold += 1
                await pets.update_butterfly(user_id, pet)
                await pets.update_butterflyG(user_id, gold)
            else:
                await call.answer('оденьте другого питомца')
        else:
            await call.answer('ошибка', show_alert=True)
            await call.message.delete()

async def GOLDdog(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    pet = await pets.dog(user_id)
    gold = await pets.dogG(user_id)
    pet = int(pet)
    gold = int(gold)
    wearpet = await pets.get_wearpet(user_id)
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        if pet > 7:
            if wearpet != 3:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил ✨собака🐶✨')
                pet -= 8
                gold += 1
                await pets.update_dog(user_id, pet)
                await pets.update_dogG(user_id, gold)
            else:
                await call.answer('оденьте другого питомца')
        else:
            await call.answer('ошибка', show_alert=True)
            await call.message.delete()

async def GOLDpig(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    pet = await pets.pig(user_id)
    gold = await pets.pigG(user_id)
    pet = int(pet)
    gold = int(gold)
    wearpet = await pets.get_wearpet(user_id)
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        if pet > 7:
            if wearpet != 5:
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил ✨свинья🐷✨')
                pet -= 8
                gold += 1
                await pets.update_pig(user_id, pet)
                await pets.update_pigG(user_id, gold)
            else:
                await call.answer('оденьте другого питомца')
        else:
            await call.answer('ошибка', show_alert=True)
            await call.message.delete()

async def GOLDcow(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    pet = await pets.cow(user_id) #
    gold = await pets.cowG(user_id)#
    pet = int(pet)
    gold = int(gold)
    wearpet = await pets.get_wearpet(user_id)
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        if pet > 7: 
            if wearpet != 8:#
                await call.message.delete()
                await call.message.answer(f'{call.message.reply_to_message.from_user.first_name} получил ✨корову🐮✨') #
                pet -= 8
                gold += 1
                await pets.update_cow(user_id, pet) #
                await pets.update_cowG(user_id, gold) #
            else:
                await call.answer('оденьте другого питомца')
        else:
            await call.answer('ошибка', show_alert=True)
            await call.message.delete()