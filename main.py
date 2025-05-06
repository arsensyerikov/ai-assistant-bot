from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN
from handlers.start import register_start_handlers
from handlers.order import register_order_handlers
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
from handlers.gpt import register_gpt_handlers
register_gpt_handlers(dp)
bot = Bot(token=BOT_TOKEN)

register_start_handlers(dp)
register_order_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)