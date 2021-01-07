import discord
from abc import abstractmethod


# Taken from https://github.com/Querela/discord-notifier-bot
class SingleTaskClient(discord.Client):
    @abstractmethod
    async def execute_task(self):
        raise NotImplementedError

    async def on_ready(self):
        await self.execute_task()
        await self.close()


class SendMessageClient(SingleTaskClient):
    def __init__(self, message: str, channel_id: int):
        super(SendMessageClient, self).__init__()
        self.message = message
        self.channel_id = channel_id

    async def execute_task(self):
        channel = self.get_channel(self.channel_id)
        await channel.send(self.message)


def send_message(bot_token: str, channel_id: int, message: str):
    client = SendMessageClient(message=message, channel_id=channel_id)
    client.run(bot_token)


def main():
    import json
    fp = '/home/kennardng/projects/notifyhub/configs/discord.json'
    with open(fp, 'r') as f:
        config = json.load(f)
    send_message(bot_token=config['bot-token'], channel_id=int(config['channel-id']), message='goodbye')


if __name__ == '__main__':
    main()