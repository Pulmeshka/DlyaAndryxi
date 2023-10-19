from aiogram import types
from ..db import db, pets
from .confog import dp
async def pets_comamnd(message: types.Message):   
    user_id = message.from_user.id
    name = message.from_user.full_name
    user = message.from_user.username
    text = ''
    text_egg = ''
    if await db.get_ban(user_id) == 1:
        await message.answer('ты в бане💥')
        return
    butterfly = await pets.butterfly(user_id)
    if butterfly > 0:
        text += f'<b><i>батерфри🦋</i> - X{butterfly}</b>\n'
    if await pets.butterflyG(user_id) > 0:
        text += f'<b><i>✨батерфри🦋✨</i> - X{await pets.butterflyG(user_id)}</b>\n'
    if await pets.default(user_id) > 0:
        text_egg += f'<b><i>обычное яйцо🥚</i> - X{await pets.default(user_id)}</b>\n'
    if await pets.dog(user_id) > 0:
        text += f'<b><i>собака🐶</i> - X{await pets.dog(user_id)}</b>\n'
    if await pets.dogG(user_id) > 0:
        text += f'<b><i>✨собака🐶✨</i> - X{await pets.dogG(user_id)}</b>\n'
    if await pets.pig(user_id) > 0:
        text += f'<b><i>свинья🐷</i> - X{await pets.pig(user_id)}</b>\n'
    if await pets.pigG(user_id) > 0:
        text += f'<b><i>✨свинья🐷✨</i> - X{await pets.pigG(user_id)}</b>\n'
    if await pets.pumpkin(user_id) > 0:
        text += f'<b><i>тыква🎃</i> - X{await pets.pumpkin(user_id)}</b>\n'
    if await pets.cow(user_id) > 0:
        text += f'<b><i>корова🐮</i> - X{await pets.cow(user_id)}</b>\n'
    if await pets.cowG(user_id) > 0:
        text += f'<b><i>✨корова🐮✨</i> - X{await pets.cowG(user_id)}</b>\n'
    if await pets.vipP(user_id) > 0:
        text += f'<b><i>VIP👑</i> - X{await pets.vipP(user_id)}</b>\n'
    if await pets.lugia(user_id) > 0:
        text += f'<b><i>лугия🪶</i> - X{await pets.lugia(user_id)}</b>\n'
    if await pets.bulbos(user_id) > 0:
        text += f'<b><i>бульбозавр🦕</i> - X{await pets.bulbos(user_id)}</b>\n'
    if await pets.tortank(user_id) > 0:
        text += f'<b><i>тортанк💦</i> - X{await pets.tortank(user_id)}</b>\n'
    if await pets.skwirt(user_id) > 0:
        text += f'<b><i>сквиртл💧</i> - X{await pets.skwirt(user_id)}</b>\n'
    if await pets.premium(user_id) > 0:
        text_egg += f'<b><i>покемон яйцо✨</i> - X{await pets.premium(user_id)}</b>\n'
    await message.answer(f'<i>твои питомцы🏡</i>:\n{text}\n\n<i>твои яйца🥚</i>:\n{text_egg}', parse_mode='HTML')
    