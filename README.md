# <p align="center"> [everyone-mention-telegram-bot](http://t.me/everyone_mention_bot)
<p align="center"> <img src="docs/logo.png" width="150"/>
<p align="center"> simple, but useful telegram bot to gather all of group members attention!
<!-- Icon made by https://www.freepik.com from https://www.flaticon.com/ -->

## Contents

* [Getting started.](#getting-started)
    * [Installation](#installation)
    * [Requirements](#requirements)
    * [Env file](#env-file)
* [Commands](#commands)
    * [`/in`](#in)
    * [`/out`](#out)
    * [`/everyone`](#everyone)

### Getting started
#### Installation
```bash
git clone https://github.com/miloszowi/everyone-mention-telegram-bot.git
pip install -r requirements.txt
python entrypoint.py
```

#### Requirements
- `python` with version specified in `runtime.txt`
- `pip` with version `20.0.2`

#### Env file
```bash
cp .env.local .env
```
and then fulfill copied `.env` file with required values
- `bot_token` - your telegram bot token from [BotFather](https://telegram.me/BotFather)
- `firebase_*`  - all of those values you can find in firebase console

### Commands
#### `/in`
Will sign you in for everyone-mentions.

![in command example](docs/in_command.png)

If you have already opted-in before, alternative reply will be displayed.

![in command when someone already opted in example](docs/in_command_already_opted_in.png)

#### `/out`
Will sign you off for everyone-mentions.

![out command example](docs/out_command.png)

If you haven't opted-in before, alternative reply will be displayed.

![out command when someone did not opt in example](docs/out_command_did_not_opt_in_before.png)

#### `/everone`
Will mention everyone that opted-in for everyone-mentions separated by spaces.

If user does not contain nickname, his ID will be present instead of nickname.

![everybody command example](docs/everyone_command.png)

If there are no users that opted-in for mentioning, alternative reply will be displayed.

![everybone noone to mention example](docs/everyone_noone_to_mention.png)
