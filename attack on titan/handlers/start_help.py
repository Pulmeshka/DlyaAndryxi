from aiogram import types
from db import db
from main import dp

keyboard = types.InlineKeyboardMarkup()
keyboard.add(types.InlineKeyboardButton(text="Смотреть гайд👁", url='https://t.me/Dolly_Chat'))

 
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Привет бро, готов ли ты играть и тратить своё время сюда, а не пойти погулять\nЕли да, то держы все команды бота - /help")
    user_id = message.from_user.id
    name = message.from_user.first_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    await message.answer(f'Ну привет <b>{name}</b> посмотри этот гайд как играть, и начинай', reply_markup=keyboard, parse_mode='HTML')

@dp.message_handler(commands=['stat'])
async def all_players_command(message: types.Message):
    user_id = message.from_user.id
    name = message.from_user.first_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    all = await db.get_all()
    await message.reply(f'статистика бота📊\nВсего игроков: {all}')