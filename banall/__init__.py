from pyrogram import Client
from pyrogram import filters
import logging
import os


STARTED = 'Black Magic Begins...'
FINISH = 'done, {} users were removed from group'
ERROR = 'something Went Wrong Please Try Again.\n\n**{}** !'


class Config:
    TOKEN=os.environ['5364821056:AAHvnJnqRgV2rBNOL6nb-yZk5dfdxAz4gKQ']
    OWNER=os.environ['Nevarevladim']
    APP_HASH=os.environ['0499f7f54f3fbb56b43acb6edf2d9696']
    APP_ID=int(os.environ['15781409'])
    LOGGER=int(os.environ['LOG_ID'])
 
    if not TOKEN:
        raise ValueError(' BOT TOKEN not set')
    
    if not APP_HASH:
        raise ValueError("API_HASH not set, set it first")

    if not APP_ID:
        raise ValueError("API_ID not set, set it first")
    if not OWNER:
        raise ValueError("OWNER_USERNAME not set, set it first")
    if not LOGGER:
        raise ValueError("LOG_ID not set set i first")
       

    
OWN_UNAME=Config.OWNER

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(
           ":memory:",
           api_id=Config.APP_ID,
           api_hash=Config.APP_HASH,
           bot_token=Config.TOKEN
)
