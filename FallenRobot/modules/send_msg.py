from pyrogram import filters
from FallenRobot import pbot as app
from pyrogram.types import Message

@app.on_message(filters.command("send"))
async def sendMessageText(app:app, msg:Message):
    if len(msg.command) == 1:
        return await msg.reply("please give some text !")
    text = msg.text.split(None, 1)[1]
    await app.send_message(msg.chat.id, text)
    await msg.delete(True)
