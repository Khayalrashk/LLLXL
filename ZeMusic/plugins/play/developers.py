import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(
    command(["المبرمج","مبرمج","مبرمج السورس","مطور السورس","خيال"])
)
async def yas(client, message):
    usr = await client.get_chat("F_A_6")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"⩹━⊷⌯⌞ 𖧊 𝐒𝐨𝐮𝐫𝐜𝐞 𝐥𝐨𝐥 𖧊 ⌝⌯⊶━⩺\n\n-› 𝙽𝙰𝙼𝙴 ¦ :{name}\n -› 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 ¦ :@{usr.username}\n -› 𝙸𝙳 ¦ :`{usr.id}`\n -› 𝙱𝙸𝙾 ¦ :{usr.bio}\n\n⩹━⊷⌯⌞ 𖧊 𝐒𝐨𝐮𝐫𝐜𝐞 𝐥𝐨𝐥 𖧊 ⌝⌯⊶━⩺", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝐊𝐡𝐚𝐲𝐚𝐥 𓏺", url=f"https://t.me/F_A_6"), 
                 ],[
                   InlineKeyboardButton(
                        "𝐒𝐨𝐮𝐫𝐜𝐞 𝐥𝐨𝐥 🧚‍♀", url=f"https://t.me/K55DD"),
                ],

            ]

        ),

    )
