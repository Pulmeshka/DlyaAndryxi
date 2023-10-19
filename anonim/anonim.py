from aiogram.types import *
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
TOKEN = "6126740167:AAEBLoKiRFEkOG9qecmMs8Rxgo6WEB3B9V4"
storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=storage)
class GetMessageStatesGroup(StatesGroup):
    get_message = State()

@dp.message_handler(commands=['start', 'help'])
async def start(message: Message, state: FSMContext):
    args = message.get_args()
    command = message.get_command()
    with open("ids.txt", "a") as f:
        if f.read == message.from_user.id:
            f.write(f"\n{message.from_user.id}")
    if (command == '/start' and not args) or (command == '/help'):
        me = await bot.me
        await message.answer(f"<b>⚡Начни получать анонимные сообщения прямо сейчас!</b>\n\nТвоя личная ссылка:\n👉<code>t.me/{me.username}?start={message.from_user.id}</code>\n\nРазмести эту ссылку ☝️ в своём профиле <b>Telegram/Instagram/TikTok</b> или других соц сетях, чтобы начать получать сообщения 💬")
    else:
        
        if str(message.from_user.id) == args.strip():
            await message.answer("⛔ Нельзя отправлять сообщения самому себе.")
        else:
            await GetMessageStatesGroup.first()
            await state.update_data(chat_id=args.strip())
            await message.answer(f"<b>🚀 Отправь анонимное сообщение человеку, который опубликовал эту ссылку!</b>\n\n✍️ Напишите сюда всё, что хотите ему передать, и через несколько секунд он получит ваше сообщение, но не будет знать от кого.\n\n👨‍💻 Отправить можно фото, видео, текст, гиф, голосовые, видеосообщения, и стикеры.\n\n<b>⚠️ Это полностью анонимно!</b>")
@dp.message_handler(state=GetMessageStatesGroup.get_message, content_types=["any"])
async def get_message(message: Message, state: FSMContext):
    data = await state.get_data()
    await state.finish()
    chat_id = data["chat_id"]
    message_id = data.get("message_id")
    me = await bot.me
    player_id = message.from_user.id
    print(player_id)
    try:
        ReplyButtonn = InlineKeyboardMarkup().add(InlineKeyboardButton("Ответить", url=f't.me/{me.username}?start={player_id}'))
        await bot.send_message(chat_id, "📨 У тебя новое анонимное сообщение:")
        await bot.copy_message(chat_id, message.chat.id, message.message_id, reply_to_message_id=message_id, reply_markup=ReplyButtonn)
    except Exception as e:
        print(e)
        await message.answer("😢 Не удалось отправить сообщение этому пользователю")
    else:
        
        await message.answer("📤 Сообщение было успешно отправлено!")
    me = await bot.me
    await message.answer(f"<b>⚡Начни получать анонимные сообщения прямо сейчас!</b>\n\nТвоя личная ссылка:\n👉<code>t.me/{me.username}?start={message.from_user.id}</code>\n\nРазмести эту ссылку ☝️ в своём профиле <b>Telegram/Instagram/TikTok</b> или других соц сетях, чтобы начать получать сообщения 💬")
# ... (ваш существующий код)
@dp.message_handler(commands=['rass123'], state="*")
async def send_custom_message(message: Message, state: FSMContext):
    ADMIN_USER_ID = [1355948406, ] #список айди админов
    if message.from_user.id in ADMIN_USER_ID:
        # Читаем текст и ссылку из файлов
        with open("text.txt", "r") as text_file, open("link.txt", "r") as link_file:
            text = text_file.read().strip()
            domen = link_file.read().strip()
        # Создаем инлайн-кнопку с ссылкой
        inline_keyboard = InlineKeyboardMarkup().add(
            InlineKeyboardButton("Перейти", url=domen)
        )
        # Читаем идентификаторы пользователей из файла
        with open("ids.txt", "r") as file:
            indef_users = [line.strip() for line in file.readlines()]
        succes_send = 0
        fail_send = 0
        # Отправляем пользовательское сообщение с инлайн-кнопкой всем разрешенным пользователям
        for ADMIN_USER_ID in indef_users:
            try:
                await bot.send_message(ADMIN_USER_ID, text, reply_markup=inline_keyboard)
                succes_send += 1
            except Exception as e:
                print(f"Не удалось отправить сообщение пользователю {ADMIN_USER_ID}: {e}")
                fail_send += 1
        
        # Отправляем сообщение с результатом
        await message.answer(f"Сообщение успешно отправлено {succes_send} пользователям. "
                             f"Не удалось отправить сообщение {fail_send} пользователям.")
    else:
        await message.answer("У вас нет разрешения использовать эту команду.")
# ... (ваш существующий код)
if __name__ == '__main__':
    print('Started!')
    executor.start_polling(dp, skip_updates=True)