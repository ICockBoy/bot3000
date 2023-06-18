import asyncio

from base import dp, bot


def add_routers():
    import routers

    dp.include_router(routers.start)


async def start():
    print("bot started!")
    add_routers()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(start())
