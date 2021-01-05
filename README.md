# Notify Me

Get your instant messaging apps to notify you when at key points of your function or when your script has
finished processing! I use this extensive for code with long processing time.

# Usage
```python
from notifyhub.messengers.telegram import send_message
from notifyhub.notifyhub import watch

CHAT_ID = '238741623'
BOT_TOKEN = '1386719865:AAG1pim7Di8pUOJYOgh_tUMLGTLI2BPHk9Q'


# send a 'hello' message via telegram
send_message(message='hello', messenger='telegram', chat_id=CHAT_ID, bot_token=BOT_TOKEN)

# get notified when your function starts/ends/crashes.
@watch(messenger="telegram", chat_id=CHAT_ID, bot_token=BOT_TOKEN)
def main():
    print(1 + 1)


main()
```


# Telegram

# Setup

Search for BotFather in telegram and use the following commands to create the bot. Take note of your bot's token
(e.g. 1017471971: AAGpJEEFZH9Mlj3_GakRtaKeMK - dmaxQVKE) and set `BOT_TOKEN` in `messengers / telegram.py`

![bot - creation](. / notify - me / extras / telegram / creating - testbot.PNG)

Then, visit `t.me / notifymetestbot` in your browser and send a message to your bot. The first message is needed to get
your `CHAT_ID`.

![bot - creation](. / notify - me / extras / telegram / say - hi.PNG)

Then, visit `https: // api.telegram.org / bot < BOT_TOKEN > /getUpdates` e.g. `https: // api.telegram.org / bot1017471971: AAGpJEEFZH9Mlj3_GakRtaKeMK - dmaxQVKE / getUpdates` to get your chat id

![chat - id - retrieval](. / notify - meextras / telegram / chat - id.PNG)

In this case, our chat id is `375385701`, and replace this value into `CHAT_ID` in `messengers / telegram`. Your bot
should be ready, to test, run `messengers / telegram.py`.

```
python setup.py install
```
