from handlers.start import router as start_router
from handlers.services import router as services_router
from handlers.order import router as order_router
from handlers.admin import router as admin_router
from handlers.request import router as request_router
import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.services import router as services_router
logging.basicConfig(
    level=logging.INFO
)

dp.include_router(services_router)
async def main():
dp.include_router(request_router)
    bot = Bot(
        token=BOT_TOKEN
    )

    dp = Dispatcher()
dp.include_router(start_router)
dp.include_router(services_router)
dp.include_router(order_router)
dp.include_router(admin_router)
dp.include_router(start_router)
    print("🤖 کافی‌نت آنلاین فعال شد")


    await dp.start_polling(
        bot
    )


if __name__ == "__main__":

    asyncio.run(main())

