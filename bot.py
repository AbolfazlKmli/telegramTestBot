import asyncio
from aiogram import Bot, Dispatcher
from handlers.start import router

TOKEN = "8035801683:AAHwAqqiKhaGiMrb36pqnhoYR9F2xfVPPeI"

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
