import asyncio
import pyrogram
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.types import InlineKeyboardButton
from ZeMusic import app
from ZeMusic.utils.database import is_on_off
from ZeMusic import app
import re
import sys
import os
import random
import config
from time import time
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters




load_dotenv()




def get_file_id(msg: Message):

    if msg.media:

        for message_type in (

            "photo",

            "animation",

            "audio",

            "document",

            "video",

            "video_note",

            "voice",

            "contact",

            "dice",

            "poll",

            "location",

            "venue",

            "sticker",

        ):

            obj = getattr(msg, message_type)

            if obj:

                setattr(obj, "message_type", message_type)

                return obj


@app.on_message(filters.regex("ا", "ايدي") & filters.group)
async def khalid(client: Client, message: Message):

    usr = await client.get_chat(message.from_user.id)

    name = usr.first_name

    bio = usr.bio




    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):

                    await message.reply_photo(photo.file_id,       caption=f"""**↯ : وفي النهاية أنتم السيئون وهم الأبرياء**
            
**↯ : اسمك : › {message.from_user.mention}**
                    
**↯ : معرفك : › @{message.from_user.username}**
                    
**↯ : ايديك : › `{message.from_user.id}`**
                    
**↯ : البايو : › \n {bio}**""", 

        reply_markup=InlineKeyboardMarkup(

            [

                [

                    InlineKeyboardButton(
                        text=config.CHANNEL_NAME, url=config.CHANNEL_LINK)
                ],

            ]

        ),

    )
    
    
