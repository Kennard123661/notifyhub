import platform
import requests
CHAT_ID = '375385701'
BOT_TOKEN = '1017471971:AAGpJEEFZH9Mlj3_GakRtaKeMK-dmaxQVKE'


def send_message(message):
    payload = {
        'chat_id': CHAT_ID,
        'text': message + '\nPC: {}'.format(platform.node()),
        'parse_mode': 'HTML'
    }
    requests.post('https://api.telegram.org/bot{}/sendMessage'.format(BOT_TOKEN),
                  data=payload)


if __name__ == '__main__':
    send_message('hello')
