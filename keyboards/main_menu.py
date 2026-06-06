from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛒 خرید اشتراک"),
            KeyboardButton(text="🔄 تمدید سرویس")
        ],
        [
            KeyboardButton(text="💳 کیف پول+شارژ"),
            KeyboardButton(text="📋 سرویس های من")
        ],
        [
            KeyboardButton(text="💰 تعرفه اشتراک ها"),
            KeyboardButton(text="👥 زیر مجموعه گیری")
        ],
        [
            KeyboardButton(text="📚 آموزش"),
            KeyboardButton(text="🎧 پشتیبانی")
        ],
        [
            KeyboardButton(text="🌐 انتخاب زبان")
        ]
    ],
    resize_keyboard=True
)
