from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

TOKEN = '6666197512:AAHkJqAUlzjYfq3LP9e4EyqVa8QejFj9Cro'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


if __name__ == '__main__':   
    from handlers import dp
    print("отдадим наши сердца!")
    executor.start_polling(dp)
