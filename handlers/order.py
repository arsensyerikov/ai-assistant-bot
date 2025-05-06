from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database.sqlite import save_order
from utils.send_to_admin import notify_admin

class OrderState(StatesGroup):
    name = State()
    email = State()
    service = State()
    comment = State()

async def start_order(message: types.Message):
    await message.reply("Ваше ім’я:")
    await OrderState.name.set()

async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.reply("Ваш email:")
    await OrderState.email.set()

async def process_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.reply("Послуга або тип замовлення:")
    await OrderState.service.set()

async def process_service(message: types.Message, state: FSMContext):
    await state.update_data(service=message.text)
    await message.reply("Додатковий коментар:")
    await OrderState.comment.set()

async def process_comment(message: types.Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()

    # Зберегти в БД
    save_order(data)

    # Сповістити адміна
    await notify_admin(message.bot, data)

    await message.reply("Дякуємо! Ваше замовлення прийнято ✅")
    await state.finish()

def register_order_handlers(dp: Dispatcher):
    dp.register_message_handler(start_order, lambda msg: msg.text == "Зробити замовлення", state="*")
    dp.register_message_handler(process_name, state=OrderState.name)
    dp.register_message_handler(process_email, state=OrderState.email)
    dp.register_message_handler(process_service, state=OrderState.service)
    dp.register_message_handler(process_comment, state=OrderState.comment)

from config import ADMIN_ID
from database.sqlite import get_last_orders

async def show_orders(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.reply("⛔ Лише адміну доступна ця команда.")
        return

    orders = get_last_orders(5)
    if not orders:
        await message.reply("Немає жодного замовлення.")
        return

    text = "🗂 Останні 5 замовлень:\n\n"
    for order in orders:
        text += (f"👤 {order[1]}\n📧 {order[2]}\n"
                 f"🛠 {order[3]}\n💬 {order[4]}\n———\n")
    
    await message.reply(text)

def register_order_handlers(dp: Dispatcher):
    ...
    dp.register_message_handler(show_orders, commands=["замовлення"])