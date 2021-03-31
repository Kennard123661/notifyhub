import inspect
import os
import json
from notifyhub.bots import discordbot, telegrambot
from functools import wraps


def _read_config_fp(config_fp: os.path):
    with open(config_fp, 'r') as f:
        config = json.load(f)
    return config


class watch(object):
    def __init__(self, config: dict = None, config_fp: os.path = None):
        super(watch, self).__init__()
        assert config is not None or config_fp is not None
        if config_fp is not None:
            config = _read_config_fp(config_fp=config_fp)
        self.config = config

    def __call__(self, func):
        @wraps(func)
        def wrapper():
            source_file = inspect.getsourcefile(func)
            source_filename = os.path.split(source_file)[-1].split('.')[:-1]

            function_name = str(func.__name__)
            function_info = '.'.join(source_filename + [function_name])
            send(message='INFO: task {} started!'.format(function_info), config=self.config)
            try:
                func()
                send(message='INFO: task {} completed'.format(function_info), config=self.config)
            except:
                send(message='ERR: task {} failed'.format(function_info), config=self.config)
                raise  # raises the exception function
        return wrapper


def send(message: str, config: dict = None, config_fp: os.path = None):
    assert config is not None or config_fp is not None, 'at least config or config_fp must be filled up'

    frame_info = inspect.stack()[1]
    filepath = os.path.abspath(frame_info[1])
    del frame_info  # drop the reference to the stack frame to avoid reference cycles

    message = '{}\nfrom {}'.format(message, filepath)
    if config_fp is not None:
        config = _read_config_fp(config_fp=config_fp)

    bot = config['bot']
    chat_id = config['chat-id']
    bot_token = config['bot-token']
    try:
        if bot == 'telegram':
            telegrambot.send(message, chat_id=chat_id, bot_token=bot_token)
        elif bot == 'discord':
            discordbot.send(message=message, chat_id=int(chat_id), bot_token=bot_token)
        else:
            raise ValueError('no such bot type')
    except Exception as e:
        _handle_exception(message=message, bot=bot, exception=e)
        return False
    return True


def _handle_exception(message: str, bot: str, exception: Exception):
    print('ERROR: Message {} failed to be send by {} bot.\n- Reason: {}'.format(message, bot, exception))


def main():
    config_dir = '/home/kennardng/projects/notifyhub/configs'
    discord_fp = os.path.join(config_dir, 'discord.json')
    telegram_fp = os.path.join(config_dir, 'telegram.json')
    send(message='hello', config_fp=discord_fp)
    send(message='hello', config_fp=telegram_fp)


if __name__ == '__main__':
    main()
