from typing import Union

import aiosqlite

from config import DB_PATH

#reg
async def insert_user(user_id: int, name: str, user: str):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("INSERT INTO users(id, name, user) VALUES (?,?,?) ON CONFLICT DO NOTHING", (user_id, name, user))
        await db.commit()

#balance coin
async def get_balance(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT coin FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None


async def update_balance(user_id: int, coin: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET coin = ? WHERE id = ?", (coin, user_id))
        await db.commit()

#balance diamond
async def get_diamond(user_id: int) -> int:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT diamond FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None

async def update_diamond(user_id: int, diamond: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET diamond = ? WHERE id = ?", (diamond, user_id))
        await db.commit()

#all players
async def get_all():
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT COUNT " "(" "id" ") " "FROM " "users")
        result = await cursor.fetchone()
        return result[0]
    
#skins
async def get_skin(user_id: int) -> Union[int, None]:
    async with aiosqlite.connect(DB_PATH) as db:
        cursor = await db.execute("SELECT skin FROM users WHERE id = ?", (user_id,))
        result = await cursor.fetchone()
        return result[0] if result is not None else None


async def update_skin(user_id: int, skin: int):
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("UPDATE users SET skin = ? WHERE id = ?", (skin, user_id))
        await db.commit()