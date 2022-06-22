from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	Hello {message.from_user.first_name }
	__➠ I ᴀᴍ ᴀ Sɪᴍᴘʟᴇ TG Rᴇɴᴀᴍᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ 🎞\n\n➠Sɪᴍᴘʟʏ Sᴇɴᴅ ᴀɴʏ Iᴍᴀɢᴇ 📷 ᴛᴏ sᴇᴛ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ 🔳\n\n➠I ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴʏ Fɪʟᴇ 📁 ᴀᴜᴅɪᴏ/ᴍᴘ3 🎶 & ᴠɪᴅᴇᴏ 🎥
	__\n\n➠ **Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ**: @robo_glitch __
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup([[
          InlineKeyboardButton("📮 Sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ 📮" ,url="https://t.me/dubbedweb"), 
	  InlineKeyboardButton("🔮 ᴏᴛʜᴇʀ ʙᴏᴛs 🔮", url="https://t.me/futurebackups")
          ],[
          InlineKeyboardButton("📣  ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ ⚡", url="https://t.me/hddubhub4u")
          ]]
          )
        )



@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__ᴡʜᴀᴛ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴅᴏ ᴡɪᴛʜ ᴛʜɪs ꜰɪʟᴇ?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("📝 Rename ",callback_data = "rename")
       ,InlineKeyboardButton("Cancel✖️",callback_data = "cancel")  ]]))
