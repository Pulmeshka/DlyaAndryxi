from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from core import handlers, create_tables
import asyncio
# PROXY_URL = "http://proxy.server:3128"
create_tables.create_all()

#ORIGINAL - 6641352325:AAFd_--9U80bHfCIjZmKI0hWlLnrcG9US4A
bot = Bot(token="6126740167:AAEBLoKiRFEkOG9qecmMs8Rxgo6WEB3B9V4")#, proxy=PROXY_URL)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(content_types=['new_chat_members'])
async def send_welcome(message: types.Message):
    bot_obj = await bot.get_me()
    bot_id = bot_obj.id
    
    for chat_member in message.new_chat_members:
        if chat_member.id == bot_id:
            await message.reply("Вау😍 Спасибо что добавили меня в ваш чудесный чат\nПропиши /start и получи гайд по командам")

async def main():
    print("Started!")
    handlers.register_handlers(dp)
    await dp.bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(allowed_updates=types.AllowedUpdates.all())

asyncio.run(main())