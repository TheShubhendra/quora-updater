import logging
import asyncio
from decouple import config
from .updater import Updater


SERVER = config("SERVER")


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(message)s",
    level=logging.DEBUG,
)


loop = asyncio.get_event_loop()
updater = Updater(SERVER)
try:
    loop.create_task(updater)
    loop.run_forever()
except KeyboardInterrupt:
    print("=" * 80)
    print("Shutting down the updater")
    tasks = asyncio.all_tasks(loop=loop)
    for t in tasks:
        t.cancel()
    group = asyncio.gather(*tasks, return_exceptions=True)
    loop.run_until_complete(group)
finally:
    loop.close()
