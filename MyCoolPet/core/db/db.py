from typing import Union

import aiosqlite

from config import DB_PATH

#new users
async def insert_user(user_id: int, name: str, user: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("INSERT INTO users(id, name, user) VALUES (?,?,?) ON CONFLICT DO NOTHING",(user_id, name, user),)
        await db.execute("INSERT INTO inventory(id) VALUES (?) ON CONFLICT DO NOTHING",(user_id,))
        await db.execute("INSERT INTO eggs(id) VALUES (?) ON CONFLICT DO NOTHING",(user_id,))
        await db.execute("INSERT INTO pets(id) VALUES (?) ON CONFLICT DO NOTHING",(user_id,))
        await db.commit()

#coin
async def get_coin(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT coin FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None

async def update_coin(user_id: int, coin: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET coin = ? WHERE id = ?", (coin, user_id))
        await db.commit()

#ban
async def get_ban(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT ban FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None

async def update_ban(user_id: int, ban: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET ban = ? WHERE id = ?", (ban, user_id))
        await db.commit()

#glove
async def get_glove(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT glove FROM inventory WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None

async def update_glove(user_id: int, glove: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE inventory SET glove = ? WHERE id = ?", (glove, user_id))
        await db.commit()

#diamond
async def get_diamond(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT diamond FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None

async def update_diamond(user_id: int, diamond: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET diamond = ? WHERE id = ?", (diamond, user_id))
        await db.commit()

# get all users
async def get_all():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT COUNT(id) FROM users")
        result = await cursor.fetchone()
        return result[0]
    
#channel bonus
async def bonus_chat(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT channelbonus FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None

async def newbonus(user_id: int, new: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET channelbonus = ? WHERE id = ?", (new, user_id))
        await db.commit()

#vip
async def vip(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT vip FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None

async def up_vip(user_id: int, vip: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET vip = ? WHERE id = ?", (vip, user_id))
        await db.commit()

#promo
async def promo(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT promo FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None

async def up_promo(user_id: int, promo: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET promo = ? WHERE id = ?", (promo, user_id))
        await db.commit()