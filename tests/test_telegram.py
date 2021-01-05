from notifyhub.messengers.telegram import send_message
from notifyhub.notifyhub import watch


def test_telegram():
    msg = "test_hello"
    chat_id = '238741623'
    bot_token = '1386719865:AAG1pim7Di8pUOJYOgh_tUMLGTLI2BPHk9Q'
    assert send_message(msg, chat_id, bot_token).status_code == 200


if __name__ == '__main__':
    test_hello()
