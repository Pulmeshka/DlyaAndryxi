from aiogram import types
from ..db import db, pets


async def DiamondCoin(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    await db.insert_user(user_id, name, user)
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    try:
        suma = message.text.split()[1]
        coin = await db.get_coin(user_id)
        diamond = await db.get_diamond(user_id)
        coin = int(coin)
        diamond = int(diamond)
        try:
            suma = int(suma)
            if diamond < suma:
                await message.answer('недостаточно кристаллов❌')
            else:
                diamond -= suma
                suma_add = suma * 700
                coin += suma_add
                await db.update_coin(user_id, coin)
                await db.update_diamond(user_id, diamond)
                await message.answer(f'перевод 💎{suma} -> ⚜{suma_add}')
        except TypeError:
            await message.answer('кристаллы должны быть числом')
    except IndexError:
        await message.answer('не ввёл суму алмазов')