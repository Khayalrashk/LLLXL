import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
import config
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","سورس لارين","السورس", "لارين ميوزك"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/41a777f089288f7ad2571.jpg",
        caption=f"""**ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ . .
 [• 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐚𝐫𝐢𝐧 ♩](https://t.me/SourceLarin)**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝐃𝐞𝐯🎖", user_id=config.OWNER_ID), 
                    
                
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=config.CHANNEL_LINK)),
                ],[
                    
                
                    InlineKeyboardButton(
                        text=config.LARIN_NAME, url=config.LARIN_LINK)),
                
        ],

            ]

        ),

    )

