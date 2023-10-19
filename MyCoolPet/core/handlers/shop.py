from aiogram import types
from ..db import db, pets
from .confog import dp

chooseButton = types.InlineKeyboardMarkup()
chooseButton.add(types.InlineKeyboardButton(text='яйца🥚', callback_data='egg'))
chooseButton.add(types.InlineKeyboardButton(text='предметы🎒', callback_data='items'))
chooseButton.add(types.InlineKeyboardButton(text='особые акции✨', callback_data='action'))

eggButton = types.InlineKeyboardMarkup()
eggButton.add(types.InlineKeyboardButton(text='обычное яйцо🥚', callback_data='EggOne'))
eggButton.add(types.InlineKeyboardButton(text='покемон яйцо✨', callback_data='EggTwo'))
eggButton.add(types.InlineKeyboardButton(text='назад🔙', callback_data='back'))

itemsButton = types.InlineKeyboardMarkup()
itemsButton.add(types.InlineKeyboardButton(text='перчатки🧤', callback_data='gloveItems'))
itemsButton.add(types.InlineKeyboardButton(text='назад🔙', callback_data='back'))

actionButton = types.InlineKeyboardMarkup()
actionButton.add(types.InlineKeyboardButton(text='VIP👑', callback_data='vipnext'))
actionButton.add(types.InlineKeyboardButton(text='назад🔙', callback_data='back'))

vipButton = types.InlineKeyboardMarkup()
vipButton.add(types.InlineKeyboardButton(text='Приобрести✅', callback_data='buyvip'))
vipButton.add(types.InlineKeyboardButton(text='назад🔙', callback_data='back'))

backButton = types.InlineKeyboardMarkup()
backButton.add(types.InlineKeyboardButton(text='назад🔙', callback_data='back'))

async def shop_comamnd(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    await message.reply('выберете что вас интересует', reply_markup=chooseButton)

async def eggs(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        await call.message.edit_text(
            '🥚цены и товары🥚\n'
            'обычное яйцо🥚 - 2000 коинов🪙(с вип - 1900)\n'
            'покемон яйцо✨ - 100 кристаллов💎(с вип - 90)\n'
            , reply_markup=eggButton)
        
async def actions(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        await call.message.edit_text(
            'VIP👑', reply_markup=actionButton)
        
async def items_shop(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        await call.message.edit_text(
            'перчатки🧤(до 100%) - 400 коинов⚜(с вип - 350)', reply_markup=itemsButton)
        
async def glove_buy(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        coin = await db.get_coin(user_id)
        coin = int(coin)
        vip = await db.vip(user_id)
        if vip == 1:
            summa = 350
        else:
            summa = 400
        summa = int(summa)
        if coin == summa or coin > summa: 
            glove = await db.get_glove(user_id)
            if glove == 100:
                await call.message.edit_text('перчатки уже с 100%', reply_markup=backButton)
                return
            glove = 100
            coin -= summa
            await db.update_coin(user_id, coin)
            await db.update_glove(user_id, glove)
            await call.message.edit_text('✅вы купили перчатки🧤', reply_markup=backButton)
        else:
            await call.message.edit_text('недостаточно монет❌', reply_markup=backButton)
        
async def egg1(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        coin = await db.get_coin(user_id)
        coin = int(coin)
        vip = await db.vip(user_id)
        if vip == 1:
            summa = 1900
        else:
            summa = 2000
        summa = int(summa)
        if coin == summa or coin > summa: 
            egg = await pets.default(user_id)
            egg += 1
            coin -= summa
            await db.update_coin(user_id, coin)
            await pets.default_up(user_id, egg)
            await call.message.edit_text('✅вы купили обычное яйцо🥚', reply_markup=backButton)
        else:
            await call.message.edit_text('недостаточно монет❌', reply_markup=backButton)

async def egg2(call: types.CallbackQuery):#
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        diamond = await db.get_diamond(user_id)#
        diamond = int(diamond)#
        vip = await db.vip(user_id)
        if vip == 1:
            summa = 90#
        else:
            summa = 100#
        summa = int(summa)
        if diamond == summa or diamond > summa: #
            egg = await pets.premium(user_id)#
            egg += 1
            diamond -= summa#
            await db.update_diamond(user_id, diamond)#
            await pets.premium_up(user_id, egg)#
            await call.message.edit_text('✅вы купили покемон яйцо✨', reply_markup=backButton)#
        else:
            await call.message.edit_text('недостаточно кристаллов❌', reply_markup=backButton)


async def back_button(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        await call.message.edit_text('выберете что вас интересует', reply_markup=chooseButton)

async def vipn(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        await call.message.edit_text(
            '<b>VIP</b> привилегия👑\n'
            'стоимость: <b>500💎</b>\n'
            'возможнсти:\n'
            '-VIP тег в профиле\n'
            '-возможность дарить вещи в магазине🎁\n'
            '-возможность подарить VIP по цене 450💎🎁\n'
            '-ексклюзивный питомец (ID - 10)\n'
            '-ексклюзивная игра <b>випер</b>\n'
            '-5000 монет🪙\n'
            '-РП команда - <b>выкинуть</b>\n'
            '-покупка вещей из магазина по скидке\n'
            'покупай не стесняйся😀'
        , parse_mode='HTML', reply_markup=vipButton)

async def buy_vip(call: types.CallbackQuery):
    user_id = call.from_user.id
    touch_id = call.message.reply_to_message.from_user.id
    touch_name = call.message.reply_to_message.from_user.first_name
    if user_id != touch_id:
        await call.answer('🙆 Не твоё', show_alert=True)
        return
    else:
        if await db.vip(user_id) == 1:
            await call.message.edit_text('Ты уже владелец вип❌', reply_markup=backButton)
            return
        diamond = await db.get_diamond(user_id)
        diamond = int(diamond)
        if diamond < 500:
            await call.message.edit_text('недостаточно средств❌', reply_markup=backButton)
            return
        diamond -= 500
        vip = 1
        coin = await db.get_coin(user_id)
        coin = int(coin)
        coin += 5000
        vip_pet = 1
        await call.message.edit_text('✅')
        await call.message.answer_sticker(f'CAACAgIAAxkBAQPrVmUkNtApKomUrpFb_Ho66CNv0O5CAAKzCwACKlBRSiyjtgnsadPWMAQ')
        await call.message.answer(f'🥳<b>{touch_name}</b> ПРИОБРЁЛ <b>VIP</b>🥂', parse_mode='HTML')

        await db.up_vip(user_id, vip)
        await db.update_coin(user_id, coin)
        await db.update_diamond(user_id, diamond)
        await pets.update_vip(user_id, vip_pet)