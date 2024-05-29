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
                
@app.on_message(filters.command(["السورس","المبرمج خيال","مبرمج السورس","خيال"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/96857cb597b588139fdd5.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[• 𝐊𝐡𝐚𝐲𝐚𝐥 𓏺](https://t.me/F_A_6)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @F_A_6 ❫
◉ 𝙸𝙳      : ❪ `5901732027` ❫
◉ 𝙱𝙸𝙾    : ❪ my world KHAYAL70.t.me ❫""",
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
