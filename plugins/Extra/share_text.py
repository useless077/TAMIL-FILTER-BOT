# Don't Remove Credit @TamilBots
# Subscribe YouTube Channel For Amazing Bot @TamilBots
# Ask Doubt on telegram @TamilSupport
#Join our Movie channel @TownBus


import os
from pyrogram import Client, filters
from urllib.parse import quote
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["share_text", "share", "sharetext"]))
async def share_text(client, message):
    sk = await client.ask(chat_id = message.from_user.id, text = "Now Send me your text.")
    if sk and (sk.text or sk.caption):
        input_text = sk.text or sk.caption
    else:
        await sk.reply_text(
            text=f"**Notice:**\n\n1. Send Any Text Messages.\n2. No Media Support\n\n**Any Question Join Support Chat**",               
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates Channel", url=f"https://t.me/TamilBots")]])
            )                                                   
        return
    await sk.reply_text(
        text=f"**Here is Your Sharing Text 👇**\n\nhttps://t.me/share/url?url=" + quote(input_text),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("♂️ Share", url=f"https://t.me/share/url?url={quote(input_text)}")]])       
    )
