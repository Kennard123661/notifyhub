from notifyhub.notifyhub import send_message
from notifyhub.notifyhub import watch

CHAT_ID = '238741623'
BOT_TOKEN = '1386719865:AAG1pim7Di8pUOJYOgh_tUMLGTLI2BPHk9Q'


def test_send_message():
    # send a 'hello' message via telegram
    assert send_message(message='hello', messenger='telegram', chat_id=CHAT_ID, bot_token=BOT_TOKEN)


def test_watch():
    # get notified when your function starts/ends/crashes.
    @watch(messenger='telegram', chat_id=CHAT_ID, bot_token=BOT_TOKEN)
    def main():
        print(1 + 1)
    main()


if __name__ == '__main__':
    test_send_message()
    test_watch()
