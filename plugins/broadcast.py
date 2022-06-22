import os
from pyrogram import Client ,filters
from helper.database import getid
ADMIN = int(os.environ.get("ADMIN", 923943045))

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"sᴛᴀʀᴛɪɴɢ ʙʀᴏᴀᴅᴄᴀsᴛ ....📣\n sᴇɴᴅɪɴɢ ᴍᴇssᴀɢᴇ ᴛᴏ ✅ {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass
