import platform
import requests

CHAT_ID = '238741623'
BOT_TOKEN = '1386719865:AAG1pim7Di8pUOJYOgh_tUMLGTLI2BPHk9Q'


def send_message(message, chat_id, bot_token):
    payload = {
        'chat_id': chat_id,
        'text': message + '\nPC: {}'.format(platform.node()),
        'parse_mode': 'HTML'
    }
    rtn = requests.post('https://api.telegram.org/bot{}/sendMessage'.format(bot_token),
                        data=payload)
    return rtn


if __name__ == '__main__':
    send_message('hello', CHAT_ID, BOT_TOKEN)
