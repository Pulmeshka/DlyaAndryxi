from aiogram import types
from ..db import db, pets
from .confog import *


async def give_pet(message: types.Message):  
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
        idpet = message.text.split()[1]
        
        try:
            idpet = int(idpet)
            
            if idpet == 1: #изменить
                if await pets.butterfly(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 1: #изменить
                        pet1 = await pets.butterfly(user_id) #изменить
                        pet2 = await pets.butterfly(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_butterfly(user_id, pet1) #изменить
                        await pets.update_butterfly(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')

            elif idpet == 2: #изменить
                if await pets.butterflyG(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 2: #изменить
                        pet1 = await pets.butterflyG(user_id) #изменить
                        pet2 = await pets.butterflyG(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_butterflyG(user_id, pet1) #изменить
                        await pets.update_butterflyG(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')

            elif idpet == 3: #изменить
                if await pets.dog(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 3: #изменить
                        pet1 = await pets.dog(user_id) #изменить
                        pet2 = await pets.dog(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_dog(user_id, pet1) #изменить
                        await pets.update_dog(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')

            elif idpet == 4: #изменить
                if await pets.dogG(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 2: #изменить
                        pet1 = await pets.dogG(user_id) #изменить
                        pet2 = await pets.dogG(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_dogG(user_id, pet1) #изменить
                        await pets.update_dogG(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')

            elif idpet == 5: #изменить
                if await pets.pig(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 5: #изменить
                        pet1 = await pets.pig(user_id) #изменить
                        pet2 = await pets.pig(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_pig(user_id, pet1) #изменить
                        await pets.update_pig(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')

            elif idpet == 6: #изменить
                if await pets.pigG(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 6: #изменить
                        pet1 = await pets.pigG(user_id) #изменить
                        pet2 = await pets.pigG(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_pigG(user_id, pet1) #изменить
                        await pets.update_pigG(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')

            elif idpet == 7: #изменить
                if await pets.pumpkin(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 7: #изменить
                        pet1 = await pets.pumpkin(user_id) #изменить
                        pet2 = await pets.pumpkin(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_pumpkin(user_id, pet1) #изменить
                        await pets.update_pumpkin(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')    

            elif idpet == 8: #изменить
                if await pets.cow(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 8: #изменить
                        pet1 = await pets.cow(user_id) #изменить
                        pet2 = await pets.cow(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_cow(user_id, pet1) #изменить
                        await pets.update_cow(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')  

            elif idpet == 9: #изменить
                if await pets.cowG(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 9: #изменить
                        pet1 = await pets.cowG(user_id) #изменить
                        pet2 = await pets.cowG(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_cowG(user_id, pet1) #изменить
                        await pets.update_cowG(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')    

            elif idpet == 10: #изменить
                if await pets.vipP(user_id) > 0: #изменить
                    await message.answer('данного питомца нельзя передавать')
                else:
                    await message.reply('у тебя нету такого питомца❌') 

            elif idpet == 11: #изменить
                if await pets.lugia(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 11: #изменить
                        pet1 = await pets.lugia(user_id) #изменить
                        pet2 = await pets.lugia(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_lugia(user_id, pet1) #изменить
                        await pets.update_lugia(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')  

            elif idpet == 12: #изменить
                if await pets.bulbos(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 12: #изменить
                        pet1 = await pets.bulbos(user_id) #изменить
                        pet2 = await pets.bulbos(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_bulbos(user_id, pet1) #изменить
                        await pets.update_bulbos(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌')  

            elif idpet == 13: #изменить
                if await pets.tortank(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 13: #изменить
                        pet1 = await pets.tortank(user_id) #изменить
                        pet2 = await pets.tortank(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_tortank(user_id, pet1) #изменить
                        await pets.update_tortank(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌') 

            elif idpet == 14: #изменить
                if await pets.skwirt(user_id) > 0: #изменить
                    if await pets.get_wearpet(user_id) != 14: #изменить
                        pet1 = await pets.skwirt(user_id) #изменить
                        pet2 = await pets.skwirt(player_id) #изменить
                        pet1 -= 1
                        pet2 += 1
                        await pets.update_skwirtl(user_id, pet1) #изменить
                        await pets.update_skwirtl(player_id, pet2) #изменить
                        await message.answer(f'<b>{name}</b> передал <b>{pets_id[idpet]}</b> игроку <b>{name2}</b>✅', parse_mode='HTML')
                    else:
                        await message.reply('одень другого питомца❌')
                else:
                    await message.reply('у тебя нету такого питомца❌') 

            else:
                if idpet > pets_all or idpet < 1:
                    await message.answer('ID такого питомца не существует❌')
                    return

        except ValueError:
            await message.answer('ID должен быть числом')
    except IndexError:
        await message.answer('ты не ввел ID питомца')