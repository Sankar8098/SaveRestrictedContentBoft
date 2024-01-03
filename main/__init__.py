#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 1512008
API_HASH = "cb1f658a4a740244a8a780ccda259118"
BOT_TOKEN = "6515769066:AAFMhcVLpDMoBk0r6IQbK1xOvqU3Dv8FYq8"
SESSION = "lhgszz--rBepXttlmG6OKsGPSwQ5UV6xcDT4f20IPdAHm3E3tT31nf245aPOcqgCa5JON7bD3PSB_7sUOW77mpMkEZOSsCz8Bd9ySkGN8u30_yIyLYAo1LSWSApfvPDyaaJtyKa1YJNNXwETy-p-7CKJFkLDjxRMaBkrKaUW8smj1RnuVDi3Y5BI7byvLToSeh_Q0YE-ENILm1CUVVU7XL-FZnU2fca8NlEpn7A0g9Ud6q2OhbZ2SpLLG55vgwAAAAFD-nzAAA"
FORCESUB = "SK_MoviesOffl"
AUTH = 5435456704

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
