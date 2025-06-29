from aiohttp import web
import os

async def handle(request):
    return web.Response(text="Бот работает ✅")

def start_web():
    port = int(os.environ.get("PORT", 10000))
    app = web.Application()
    app.router.add_get("/", handle)
    web.run_app(app, port=port)
