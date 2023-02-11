
# Chatgpt Discord bot

A Discord bot that implements the ChatGPT AI intelligence



## Requirements

These modules need to be installed:

```bash
$ pip install -U Flask
$ python3 -m pip install -U discord.py
$ pip install openai
```
    
## TOKENS
To obtain the OpenAI API key, you will need to have an account and go to the following page:

https://platform.openai.com/account/api-keys

And for Discord, you will need to create an application from the following page:

https://discord.com/developers/applications

![alt text](https://github.com/AguuZzz/ChatGPT-DiscordBot/blob/main/screenshot.png?raw=true)

And paste both keys in:

```PYTHON
openai.api_key = TOKEN
```

```PYTHON
bot.run(TOKEN)
```
with quotes
