from aiogram import types
from ..db import db, pets
from .confog import dp

async def wear_list_command(message: types.Message): 
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    wearpet = await pets.get_wearpet(user_id)
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    #ДОБАВИТЬ ТУТ
    text = ''
    if await pets.butterfly(user_id) > 0 and wearpet != 1:
        text += 'батерфри🦋 - <code>/wear 1</code>\n'
    if await pets.butterflyG(user_id) > 0 and wearpet != 2:
        text += '✨батерфри🦋✨ - <code>/wear 2</code>\n'
    if await pets.dog(user_id) > 0 and wearpet != 3:
        text += 'собака🐶 - <code>/wear 3</code>\n'
    if await pets.dogG(user_id) > 0 and wearpet != 4:
        text += '✨собака🐶✨ - <code>/wear 4</code>\n'
    if await pets.pig(user_id) > 0 and wearpet != 5:
        text += 'свинья🐷 - <code>/wear 5</code>\n'
    if await pets.pigG(user_id) > 0 and wearpet != 6:
        text += '✨свинья🐷✨ - <code>/wear 6</code>\n'
    if await pets.pumpkin(user_id) > 0 and wearpet != 7:
        text += 'тыква🎃 - <code>/wear 7</code>\n'
    if await pets.cow(user_id) > 0 and wearpet != 8:
        text += 'корова🐮 - <code>/wear 8</code>\n'
    if await pets.cowG(user_id) > 0 and wearpet != 9:
        text += '✨корова🐮✨ - <code>/wear 9</code>\n'
    if await pets.vipP(user_id) > 0 and wearpet != 10:
        text += 'VIP👑 - <code>/wear 10</code>\n'
    if await pets.lugia(user_id) > 0 and wearpet != 11:
        text += 'лугия🪶 - <code>/wear 11</code>\n'
    if await pets.bulbos(user_id) > 0 and wearpet != 12:
        text += 'бульбозавр🦕 - <code>/wear 12</code>\n'
    if await pets.tortank(user_id) > 0 and wearpet != 13:
        text += 'тортанк💦 - <code>/wear 13</code>\n'
    if await pets.skwirt(user_id) > 0 and wearpet != 14:
        text += 'сквиртл💧 - <code>/wear 14</code>\n'
    #отправляем сообщение
    await message.reply(f'выберете какого питомца желаете одеть:\n{text}', parse_mode='HTML')


async def wear_pet_command(message: types.Message): 
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    wearpet = await pets.get_wearpet(user_id)
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    try:     
        pet_wear = message.text.split()[1]
        try:
            pet_wear = int(pet_wear)

            if pet_wear == 1:#
                if await pets.butterfly(user_id) > 0:#
                    if wearpet != 1:#
                        await message.answer(f'<b>{name}</b> одел <b>батерфри</b>', parse_mode='HTML')#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')
            
            elif pet_wear == 2:
                if await pets.butterflyG(user_id) > 0:#
                    if wearpet != 2:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>золотого батерфри</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 3:
                if await pets.dog(user_id) > 0:#
                    if wearpet != 3:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>собаку</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 4:
                if await pets.dogG(user_id) > 0:#
                    if wearpet != 4:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>золотую собаку</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 5:
                if await pets.pig(user_id) > 0:#
                    if wearpet != 5:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>свинью</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 6:
                if await pets.pigG(user_id) > 0:#
                    if wearpet != 6:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>золотую свинью</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 7:
                if await pets.pumpkin(user_id) > 0:#
                    if wearpet != 7:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>тыкву</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 8:
                if await pets.cow(user_id) > 0:#
                    if wearpet != 8:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>корову</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 9:
                if await pets.cowG(user_id) > 0:#
                    if wearpet != 9:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>золотую корову</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 10:
                if await pets.vipP(user_id) > 0:#
                    if wearpet != 10:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>VIP👑</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 11:#
                if await pets.lugia(user_id) > 0:#
                    if wearpet != 11:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>лугия</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 12:#
                if await pets.bulbos(user_id) > 0:#
                    if wearpet != 12:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>бульбозавра</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 13:#
                if await pets.tortank(user_id) > 0:#
                    if wearpet != 13:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>тортанка</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

            elif pet_wear == 14:#
                if await pets.skwirt(user_id) > 0:#
                    if wearpet != 14:#
                        wearpet = pet_wear
                        await pets.update_wearpet(user_id, wearpet)
                        await message.answer(f'<b>{name}</b> одел <b>сквиртла</b>', parse_mode='HTML')#
                    else:
                        await message.answer('одень другого питомца❌')
                else:
                    await message.answer('у тебя нету такого питомца❌')

        except ValueError:
            await message.answer('ID должен быть числом')
    except IndexError:
        await message.answer('ты не ввел ID питомца')