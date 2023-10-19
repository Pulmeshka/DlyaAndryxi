from aiogram import types, Bot
from ..db import db, pets
from .confog import dp, wear_pet

bot = Bot(token="6641352325:AAFd_--9U80bHfCIjZmKI0hWlLnrcG9US4A")

async def start(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    keyboardhelp = types.InlineKeyboardMarkup()
    keyboardhelp.add(types.InlineKeyboardButton(text='полный гайд⁉️', url='https://telegra.ph/Gajd-MyCoolPet-bot-10-09'))
    await message.answer('<a href="https://t.me/MyCoolPetNews"><b>КАНАЛ БОТА</b></a>\n<a href="https://t.me/MyCoolPetCHAT"><b>ЧАТ БОТА</b></a>', parse_mode='HTML', reply_markup=keyboardhelp)
    

async def me(message: types.Message):  
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    wearpet = await pets.get_wearpet(user_id)
    diamond = await db.get_diamond(user_id)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    coin = await db.get_coin(user_id)
    if await db.vip(user_id) == 1:
        viptext = '👑VIP👑'
    else:
        viptext = ''
    await message.answer_sticker(f'{wear_pet[wearpet]}')
    keyboardmoney = types.InlineKeyboardMarkup()
    keyboardmoney.add(types.InlineKeyboardButton(text=f'имя: {name}', callback_data='error'))
    keyboardmoney.add(types.InlineKeyboardButton(text=f'монеты⚜: {coin}', callback_data='error'))
    keyboardmoney.add(types.InlineKeyboardButton(text=f'кристаллы💎: {diamond}', callback_data='error'))
    keyboardmoney.add(types.InlineKeyboardButton(text='добавить бота в чат➕', url='https://t.me/MyCoolPet_bot?startgroup='))
    await message.reply(
        f'{viptext}\n'
        f'⇒ <code><b>{user_id}</b></code>'
        , parse_mode='HTML', reply_markup=keyboardmoney)


@dp.callback_query_handler(text="error")
async def error(call: types.CallbackQuery):
    await call.answer('кнопка ничего не делает💛')

async def all_users(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    all_us = await db.get_all()
    await message.answer(f'в <b>MyCoolPet</b> зарегистрировано <b>{all_us}</b> игроков🕹', parse_mode='HTML')

# async def channel_bonus(message: types.Message):   
#     user_id = message.from_user.id
#     name = message.from_user.full_name
#     user = message.from_user.username
#     await db.insert_user(user_id, name, user)
#     result = await bot.get_chat_member(chat_id='-1001881267377', user_id=user_id)
#     bonus = await db.bonus_chat(user_id)
#     if result.status == 'left':
#         await message.answer('❌Ты не подписан на канал❌\n@MyCoolPetNews')
#         return
#     if result.status != 'member' or result.status != 'left':
#         await message.answer('ERROR❌')
#         return
#     if result.status == 'member':
#         if bonus == 1:
#             await message.answer('ты уже получал награду❌')
#             return
#         await message.answer('ты получил 10 кристаллов, спасибо за подписку✅')
#         diamond = await db.get_diamond(user_id)
#         diamond = int(diamond)
#         diamond += 10
#         bonus = 1
#         await db.newbonus(user_id, bonus)
#         await db.update_diamond(user_id, diamond)

async def donate(message: types.Message):  
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥\nДля получение разбана тебе нужно 300💎, писать к: @Pulmeshka_of')
        return
    await message.answer(
        'Привет дорогой любитель питомцев, вижу ты решил заглянуть в донат меню\n'
        'Кристаллы стоят по курсу <b>1 грн = 5 кристаллов</b>\n'
        'Минимальная покупка от 20 грн\n'
        'По поводу других валют нужно уточнять\n'
        'Если желаешь приобрести кристаллы - пиши к <b>@Pulmeshka_of</b>'
        , parse_mode='HTML')
    
async def bot_command(message: types.Message):  
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    await message.reply('Мурр, на месте')

async def promo_command(message: types.Message):  
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user) 
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    diamond = await db.get_diamond(user_id)
    coin = await db.get_coin(user_id)
    diamond = int(diamond)
    coin = int(coin)
    try:
        promokod = message.text.split()[1]
        if await db.promo(user_id) == 1:
            await message.answer('Ты уже вводил промо❌')
            return
        if promokod == 'OpenBot':
            diamond += 500
            coin += 2000
            promok = 1
            await db.up_promo(user_id, promok)
            await db.update_coin(user_id, coin)
            await db.update_diamond(user_id, diamond)
            await message.answer('Промокод найден✅\n<b>Было получено:</b>\n<b>500💎\n2000🪙</b>', parse_mode='HTML')
        else:
            await message.answer('Данного промокода не существует🙅🏻')
    except IndexError:
        await message.answer('Ты не ввёл промо❌')
