import logging
import aiohttp


class NetworkInterface:
    def __init__(self, updater):
        self.updater = updater
        self.server = updater.server
        self.logger = logging.getLogger(__name__)

    async def register(self):
        self.logger.info("Registering the updater")
        async with aiohttp.ClientSession() as session:
            req = await session.get(self.server + "/registerUpdater")
            return await req.json()

    async def send_event(self, payload):
        self.logger.info("Sending event")
        async with aiohttp.ClientSession() as session:
            self.logger.debug(payload)
            req = await session.post(self.server + "/update", data=payload)
