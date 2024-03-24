from pyrogram import filters
from FallenRobot.config import AUTH

@app.on_message(filters.command("auth"))
async def sudo(app, message):
    if message.reply_to_message.from_user.id not in AUTH:
        AUTH.append(user_id)
    else:
        await message.reply("ᴜsᴇʀ ᴀᴅᴅᴇᴅ ᴛᴏ ᴀᴜᴛʜ ᴜsᴇʀs.")

@app.on_edited_message(filters.text)
async def ded(app, m):
    if m.from_user.id not in AUTH:
        return await app.delete_messages(m.chat.id, m.id)
