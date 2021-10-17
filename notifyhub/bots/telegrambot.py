import platform
import requests


def send(message: str, chat_id: int, bot_token: str):
    payload = {
        'chat_id': chat_id,
        'text': message + '\nPC: {}'.format(platform.node()),
        'parse_mode': 'HTML'
    }
    rtn = requests.post('https://api.telegram.org/bot{}/sendMessage'.format(bot_token),
                        data=payload)
    return rtn


if __name__ == '__main__':
    pass
