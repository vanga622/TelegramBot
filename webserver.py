from aiohttp import web
import os

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

    # Поддерживать веб-сервер живым
    while True:
        await asyncio.sleep(3600)
