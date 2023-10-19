from aiogram import types
from ..db import db, pets
from .confog import dp, wear_pet

sellButton = types.InlineKeyboardMarkup()
sellButton.add(types.InlineKeyboardButton(text='Продать💰', callback_data='sell'))

async def torgoves_command(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    await message.reply('привет, я торговец хожу по городам и скупаю золотых собак, не желаешь продать свою?\n1 собака = 1 кристалл и 200 коинов', reply_markup=sellButton)


async def sell_gold_dog(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    wearpet = await pets.get_wearpet(user_id)
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        if await pets.dogG(user_id) > 0:
            if wearpet != 4:
                pet = await pets.dogG(user_id)
                pet -= 1
                diamond = await db.get_diamond(user_id)
                diamond += 1
                coin = await db.get_coin(user_id)
                coin += 200
                await pets.update_dogG(user_id, pet)
                await db.update_diamond(user_id, diamond)
                await db.update_coin(user_id, coin)
                await call.message.edit_text('спасибо за продажу🩲')
            else:
                await call.message.edit_text('одень другого питомца')
        else:
            await call.answer('ой ой, а где же твоя собака🙁', show_alert=True)
            await call.message.delete()   