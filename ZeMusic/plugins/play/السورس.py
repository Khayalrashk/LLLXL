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
        photo=f"https://graph.org/file/57036e277059ef8608dd3.jpg",
        caption=f"""<b>  <b>\n<a href="https://t.me/SOURCELARIN"> ➮ 𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐋𝐚𝐫𝐢𝐧 🎧</a></b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝐃𝐞𝐯🎖", user_id=config.OWNER_ID), 
                    
                
                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=config.CHANNEL_LINK),
                ],[
                    
                
                    InlineKeyboardButton(
                        text=config.LARIN_NAME, url=config.LARIN_LINK),
                
        ],

            ]

        ),

    )

