import asyncio
from bot import run_bot
from webserver import start_web
import threading

# Запускаем веб-сервер в отдельном потоке
threading.Thread(target=start_web).start()

# Запускаем Telegram-бота
asyncio.run(run_bot())