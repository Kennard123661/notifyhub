import discord
import asyncio
from abc import abstractmethod
import yaml


class SingleTaskClient(discord.Client):
    @abstractmethod
    async def execute_task(self):
        raise NotImplementedError

    async def on_ready(self):
        await self.execute_task()
        await self.logout()


class SendMessageClient(SingleTaskClient):
    def __init__(self, message: str, channel_id: int):
        super(SendMessageClient, self).__init__()
        self.message = message
        self.channel_id = channel_id

    async def execute_task(self):
        channel = self.get_channel(self.channel_id)
        await channel.send(self.message)


async def _send_message(bot_token: str, chat_id: int, message: str):
    client = SendMessageClient(message=message, channel_id=chat_id)
    await client.login(token=bot_token)
    await client.connect()


def send(bot_token: str, chat_id: int, message: str):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(_send_message(bot_token=bot_token, chat_id=chat_id, message=message))


def main():
    import json
    fp = '/mnt/Data/Documents/Projects/Personal/notifyhub/configs/discord.yaml'
    with open(fp, 'r') as f:
        config = yaml.full_load(f)
    send(bot_token=config['bot-token'], chat_id=int(config['chat-id']), message='gb0')
    send(bot_token=config['bot-token'], chat_id=int(config['chat-id']), message='gb1')


if __name__ == '__main__':
    main()
