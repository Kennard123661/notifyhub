# NotifyHub

Library to send you messages from your python scripts.

## Setup

### For contributors:

```bash
conda create -n notifyhub python==3.6.6  # works with RPi
conda activate notifyhub
pip install -r requirements.txt
```

### For users:

```bash
cd ..  # parent directory
pip install notifyhub
```

## Usage

```python
from notifyhub import send, watch

CONFIG_FP = '<CONFIG_FP>'  # config .json file
send(message="hello there", config_fp=CONFIG_FP)  # sends message 'hello there'


# watch program to check if it crashes/completes
@watch(config_fp=CONFIG_FP)
def main():
    print('do something')
```

### Telegram

Your telegram configuration file should look like:
```
{
    "bot": "telegram",
    "bot-token": "<BOT TOKEN>",
    "chat-id": <CHAT ID>
}
```


### Discord
Your discord configuration file should look like:
```
{
    "bot": "discord",
    "bot-token": "<BOT TOKEN>",
    "chat-id": <CHANNEL ID>
}
```
