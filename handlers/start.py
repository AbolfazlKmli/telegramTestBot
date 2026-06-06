from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.main_menu import main_menu

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    text = (
        "🤖 به ربات مدیریت فروش VPN خوش آمدید!\n\n"
        "لطفاً یکی از گزینه‌های زیر را انتخاب کنید:"
    )

    await message.answer(text=text, reply_markup=main_menu)
