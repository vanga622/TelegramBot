import asyncio
from bot import run_bot
from webserver import run_web_app

async def main():
    await asyncio.gather(
        run_bot(),
        run_web_app()
    )

if __name__ == "__main__":
    asyncio.run(main())
