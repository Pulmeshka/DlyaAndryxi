from typing import Union

import aiosqlite

from config import DB_PATH
#----------------------PETS-----------------------

# get wear pet
async def get_wearpet(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT wearpet FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_wearpet(user_id: int, wearpet: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET wearpet = ? WHERE id = ?", (wearpet, user_id))
        await db.commit()

# butterfly
async def butterfly(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT butterfly FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_butterfly(user_id: int, butterfly: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET butterfly = ? WHERE id = ?", (butterfly, user_id))
        await db.commit()
# butterfly GOLD
async def butterflyG(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT butterflyGOLD FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_butterflyG(user_id: int, butterflyG: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET butterflyGOLD = ? WHERE id = ?", (butterflyG, user_id))
        await db.commit()

# dog
async def dog(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT dog FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_dog(user_id: int, dog: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET dog = ? WHERE id = ?", (dog, user_id))
        await db.commit()
# dog GOLD
async def dogG(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT dogGOLD FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_dogG(user_id: int, dogG: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET dogGOLD = ? WHERE id = ?", (dogG, user_id))
        await db.commit()

# pig
async def pig(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT pig FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_pig(user_id: int, pig: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET pig = ? WHERE id = ?", (pig, user_id))
        await db.commit()
# pig GOLD
async def pigG(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT pigGOLD FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_pigG(user_id: int, pigG: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET pigGOLD = ? WHERE id = ?", (pigG, user_id))
        await db.commit()

# pumpkin
async def pumpkin(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT pumbkin FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_pumpkin(user_id: int, pumpkin: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET pumbkin = ? WHERE id = ?", (pumpkin, user_id))
        await db.commit()

# cow
async def cow(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT cow FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_cow(user_id: int, cow: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET cow = ? WHERE id = ?", (cow, user_id))
        await db.commit()
# cow GOLD
async def cowG(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT cowGOLD FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_cowG(user_id: int, cowG: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET cowGOLD = ? WHERE id = ?", (cowG, user_id))
        await db.commit()

# vip
async def vipP(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT vip FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_vip(user_id: int, vipP: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET vip = ? WHERE id = ?", (vipP, user_id))
        await db.commit()

# lugia
async def lugia(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT lugia FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_lugia(user_id: int, lugia: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET lugia = ? WHERE id = ?", (lugia, user_id))
        await db.commit()

# bulbosawr
async def bulbos(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT bulbosour FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_bulbos(user_id: int, bulbo: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET bulbosour = ? WHERE id = ?", (bulbo, user_id))
        await db.commit()

# tortank
async def tortank(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT tortank FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_tortank(user_id: int, tortanks: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET tortank = ? WHERE id = ?", (tortanks, user_id))
        await db.commit()

# skwirtl
async def skwirt(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT skwirtl FROM pets WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def update_skwirtl(user_id: int, skwirtl: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE pets SET skwirtl = ? WHERE id = ?", (skwirtl, user_id))
        await db.commit()



#--------------------EGGS------------

# default egg
async def default(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT defaultEgg FROM eggs WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def default_up(user_id: int, egg: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE eggs SET defaultEgg = ? WHERE id = ?", (egg, user_id))
        await db.commit()

# premium egg
async def premium(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT premiumEgg FROM eggs WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None
async def premium_up(user_id: int, egg: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE eggs SET premiumEgg = ? WHERE id = ?", (egg, user_id))
        await db.commit()