import os
import asyncio  
from aiohttp import web

async def handle(request):
    return web.Response(text="Бот работает ✅")

async def run_web_app():
    app = web.Application()
    app.router.add_get("/", handle)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    print(f"🔌 Web server listening on port {port}")
    await site.start()

    # Поддерживаем приложение в живом состоянии
    while True:
        await asyncio.sleep(3600)
