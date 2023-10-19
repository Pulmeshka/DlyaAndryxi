from aiogram import types
from ..db import db, pets
from .confog import *

async def admin_comamnds(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if user_id not in admin_id_list:
        await message.answer('куда мы лезим?')
        return
    await message.answer(
        'админ команды\n'
        '-MyBan/МайБан/блокнуть - заблокировать пользователя\n'
        '-MyUnban/Майанбан/разблокать - разблокировать пользователя\n'
        '-выдать/give <1-коины/2-кристаллы> <сума> - выдать нужную валюту(в ответ на сообщение) 1 - выдача коинов, 2 - выдача кристаллов\n'
        '-givepet/выдать пет <ID питомца> - выдать любого питомца по его ID(в ответ на сообщение)')

async def ban_player(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if user_id not in admin_id_list:
        await message.answer('куда мы лезим?')
        return
    if not message.reply_to_message:
        await message.answer('на сообщение ответь')
        return
    player_id = message.reply_to_message.from_user.id
    name2 = message.reply_to_message.from_user.full_name
    user2 = message.reply_to_message.from_user.username
    await db.insert_user(player_id, name2, user2)
    if message.reply_to_message.from_user.is_bot:
        await message.answer('я брадка не забаню')
        return
    if player_id == user_id:
        await message.answer('мне точно нужно тебя забанить?')
        return
    ban = await db.get_ban(player_id)
    if ban == 1:
        await message.answer('пользователь уже в бане')
        return
    if player_id in admin_id_list:
        await message.answer('не трогай админа🛑')
        return
    ban = 1
    await db.update_ban(player_id, ban)
    await message.answer('✅пользователь забанен✅')

async def unban_player(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if user_id not in admin_id_list:
        await message.answer('куда мы лезим?')
        return
    if not message.reply_to_message:
        await message.answer('на сообщение ответь')
        return
    player_id = message.reply_to_message.from_user.id
    name2 = message.reply_to_message.from_user.full_name
    user2 = message.reply_to_message.from_user.username
    await db.insert_user(player_id, name2, user2)
    if message.reply_to_message.from_user.is_bot:
        await message.answer('брадки в бане не сидят')
        return
    if player_id == user_id:
        await message.answer('а ты тут причём?')
        return
    ban = await db.get_ban(player_id)
    if ban == 0:
        await message.answer('пользователь не забанен')
        return
    ban = 0
    await db.update_ban(player_id, ban)
    await message.answer('✅пользователь разблокирован✅')
    
async def give_coin_diamond(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if user_id not in admin_id_list:
        await message.answer('куда мы лезим?')
        return
    if not message.reply_to_message:
        await message.answer('на сообщение ответь')
        return
    player_id = message.reply_to_message.from_user.id
    name2 = message.reply_to_message.from_user.full_name
    user2 = message.reply_to_message.from_user.username
    await db.insert_user(player_id, name2, user2)
    if message.reply_to_message.from_user.is_bot:
        await message.answer('❌')
        return
    try:
        coin_or_diamond = message.text.split()[1]
        try:
            coin_or_diamond = int(coin_or_diamond)
            try:
                suma = message.text.split()[2]
                player_coin = await db.get_coin(player_id)
                player_diamond = await db.get_diamond(player_id)
                player_coin = int(player_coin)
                try:
                    suma = int(suma)
                    if coin_or_diamond == 1:
                        player_coin += suma
                        await db.update_coin(player_id, player_coin)
                        await message.answer(f'<b>{name2}</b> было получено <b>{suma}</b> ⚜коинов⚜\nадминистратор: <b>{name}</b>', parse_mode='HTML')
                    elif coin_or_diamond == 2:
                        player_diamond = int(player_diamond)
                        player_diamond += suma
                        await db.update_diamond(player_id, player_diamond)
                        await message.answer(f'<b>{name2}</b> было получено <b>{suma}</b> 💎кристаллов💎\nадминистратор: <b>{name}</b>', parse_mode='HTML')
                    else:
                        await message.answer('❌')
                except TypeError:
                    await message.answer('❌')
            except IndexError:
                await message.answer('ты не ввёл суму')
        except ValueError:
            await message.answer('❌')
    except IndexError:
        await message.answer('выбери валюту выдачи')



async def give_pet2(message: types.Message):  
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if user_id not in admin_id_list:
        await message.answer('ты не админ')
        return
    if not message.reply_to_message:
        await message.answer('ты не ответил на сообщение')
        return
    player_id = message.reply_to_message.from_user.id
    name2 = message.reply_to_message.from_user.full_name
    user2 = message.reply_to_message.from_user.username
    await db.insert_user(player_id, name2, user2)
    if message.reply_to_message.from_user.is_bot:
        await message.answer('❌')
        return
    try:     
        idpet = message.text.split()[1]
        
        try:
            idpet = int(idpet)

            if idpet == 1: #изменить
                pet2 = await pets.butterfly(player_id) #изменить
                pet2 += 1
                await pets.update_butterfly(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 2: #изменить
                pet2 = await pets.butterflyG(player_id) #изменить
                pet2 += 1
                await pets.update_butterflyG(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')

            if idpet == 3: #изменить
                pet2 = await pets.dog(player_id) #изменить
                pet2 += 1
                await pets.update_dog(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 4: #изменить
                pet2 = await pets.dogG(player_id) #изменить
                pet2 += 1
                await pets.update_dogG(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 5: #изменить
                pet2 = await pets.pig(player_id) #изменить
                pet2 += 1
                await pets.update_pig(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 6: #изменить
                pet2 = await pets.pigG(player_id) #изменить
                pet2 += 1
                await pets.update_pigG(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 7: #изменить
                pet2 = await pets.pumpkin(player_id) #изменить
                pet2 += 1
                await pets.update_pumpkin(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 8: #изменить
                pet2 = await pets.cow(player_id) #изменить
                pet2 += 1
                await pets.update_cow(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 9: #изменить
                pet2 = await pets.cowG(player_id) #изменить
                pet2 += 1
                await pets.update_cowG(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 10: #изменить
                pet2 = await pets.vipP(player_id) #изменить
                pet2 += 1
                await pets.update_vip(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 11: #изменить
                pet2 = await pets.lugia(player_id) #изменить
                pet2 += 1
                await pets.update_lugia(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 12: #изменить
                pet2 = await pets.bulbos(player_id) #изменить
                pet2 += 1
                await pets.update_bulbos(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 13: #изменить
                pet2 = await pets.tortank(player_id) #изменить
                pet2 += 1
                await pets.update_tortank(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            if idpet == 14: #изменить
                pet2 = await pets.skwirt(player_id) #изменить
                pet2 += 1
                await pets.update_skwirtl(player_id, pet2) #изменить
                await message.answer(f'<b>{name2}</b> получил <b>{pets_id[idpet]}</b>\nадмин <b>{name}</b>', parse_mode='HTML')
            
            else:
                if idpet > pets_all or idpet < 1:
                    await message.answer('ID такого питомца не существует❌')
                    return

        except ValueError:
            await message.answer('ID должен быть числом')
    except IndexError:
        await message.answer('ты не ввел ID питомца')