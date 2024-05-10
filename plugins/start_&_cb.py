"""
Apache License 2.0
Copyright (c) 2022 @Digital_Botz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Telegram Link : https://t.me/Digital_Botz 
Repo Link : https://github.com/DigitalBotz/Digital-Rename-Bot
License Link : https://github.com/RknDeveloper/Digital-Rename-Bot/blob/main/LICENSE
"""

import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from helper.database import db
from config import Config, rkn  
  
start_button = InlineKeyboardMarkup([[        
        InlineKeyboardButton('Uᴩᴅᴀ𝚃ᴇꜱ', url='https://t.me/Digital_Botz'),
        InlineKeyboardButton('Sᴜᴩᴩᴏʀ𝚃', url='https://t.me/DigitalBotz_Support')
        ],[
        InlineKeyboardButton('Aʙᴏυᴛ', callback_data='about'),
        InlineKeyboardButton('Hᴇʟᴩ', callback_data='help')
        ],[
        InlineKeyboardButton('💸 ᴜᴘɢʀᴀᴅᴇ ᴛᴏ ᴘʀᴇᴍɪᴜᴍ 💸', callback_data='upgrade')
         ]])

@Client.on_message(filters.private & filters.command("start"))
async def start(client, message):
    user = message.from_user
    await db.add_user(client, message) 
    if Config.RKN_PIC:
        await message.reply_photo(Config.RKN_PIC, caption=rkn.START_TXT.format(user.mention), reply_markup=start_button)       
    else:
        await message.reply_text(text=rkn.START_TXT.format(user.mention), reply_markup=start_button, disable_web_page_preview=True)
   

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=rkn.START_TXT.format(query.from_user.mention),
            disable_web_page_preview=True,
            reply_markup = start_button
        )
    elif data == "help":
        await query.message.edit_text(
            text=rkn.HELP_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("°.Oᴡɴᴇʀ.°", url="https://t.me/RknDeveloperr")
              ],[
               
                InlineKeyboardButton("Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("Bᴀᴄᴋ", callback_data = "start")
                  ]])            
        )
    elif data == "about":
        await query.message.edit_text(
            text=rkn.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("💞 𝚂ᴏᴜʀᴄᴇ 𝙲ᴏᴅᴇ 💞", callback_data = "source_code")
            ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
                ],[
                InlineKeyboardButton('🎬 𝙹𝙾𝙸𝙽 𝙼𝙾𝚅𝙸𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 🎬', url='https://t.me/CG_OF_MOVIES')
            ]])            
        )
    elif data == "upgrade":
        await query.message.edit_text(
            text=rkn.UPGRADE,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
             InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")]])) 
    elif data == "source_code":
        await query.message.edit_text(
            text=rkn.DEV_TXT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([[
                #⚠️ don't change source code & source link ⚠️ #
                InlineKeyboardButton("💞 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ 💞", url="https://github.com/RknDeveloper/Rkn-rename-bot-V3")
            ],[
                InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data = "close"),
                InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
                 ]])          
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
            await query.message.continue_propagation()
        except:
            await query.message.delete()
            await query.message.continue_propagation()

