# (c) @RoyalKrrishna

import os
import asyncio
import traceback
from dotenv import (
    load_dotenv
)
from pyrogram import (
    Client,
    filters,
    idle
)
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from pyrogram.errors import (
    MessageNotModified
)
from core.search_video import search_vivdisk_videos

if os.path.exists("configs.env"):
    load_dotenv("configs.env")


class Configs(object):
    API_ID = int(os.environ.get("API_ID", 0))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    VIVDISK_USERNAME = os.environ.get("vivdisk_email", "")
    VIVDISK_PASSWORD = os.environ.get("vivdisk_PASSWORD", "")
    MAX_RESULTS = int(os.environ.get("MAX_RESULTS", 5))
    # Which Disk Domain?
    vivdisk_DOMAIN = [
        
       
        "https://vivdisk.com/"
    ]
    vivdisk_DOMAIN = os.environ.get("vivdisk_DOMAIN", vivdisk_DOMAIN[2])


vivdiskBot = Client(
    session_name=":memory:",
    api_id=Configs.API_ID,
    api_hash=Configs.API_HASH,
    bot_token=Configs.BOT_TOKEN
)


@vivdiskBot.on_message(filters.command("start") & ~filters.edited)
async def start_handler(_, m: Message):
    await m.reply_text("**Hiii! 😀\n\n🔸I'm Simple Movie Search Bot 🔍\n\n🔹I Can Search Movies For You 🎥\n\n🔸Just Type /request Movie Name 👇🏻\n\n🔹Example - /request Dhoom 2 ✅\n\n🔸Porn Ban Here! 🔞\n\n🔹You Can Add Me To Groups 💬\n\n🔸Devloped By @sigma_male_007 🕵️**", quote=True)


@PDiskBot.on_message(filters.command("request", prefixes=["#", "/"]) & ~filters.edited, group=-1)
async def text_handler(_, m: Message):
    if len(m.command) < 2:
        return await m.reply_text("Type /request Then Movie Name❗")
    editable = await m.reply_text("Searching Your Movie🍿\nPlease Wait...⏳", quote=True)
    response = await search_pdisk_videos(m.text.split(" ", 1)[-1], Configs.vivdisk_email, Configs.vivdisk_PASSWORD)
    if isinstance(response, Exception):
        traceback.print_exc()
        try: await editable.edit("Network Problem",
                                 reply_markup=InlineKeyboardMarkup([
                                     [InlineKeyboardButton("Report", url="https://t.me/sigma_male_007")]
                                 ]))
        except MessageNotModified: pass
    elif not response["data"]["list"]:
        try: await editable.edit("Not Found🚫\nCheck Spelling On Google🔍")
        except MessageNotModified: pass
    else:
        data = response["data"]["list"]
        text = ""
        count = 0
        for i in range(len(data)):
            if count > Configs.MAX_RESULTS:
                break
            count += 1
            text += f"**♻️ Title:** `{data[i]['title']}`\n" \
                    f"**🔗 Link:** {Configs.vivdisk_DOMAIN + 'share-video?videoid=' + data[i]['share_link'].split('=', 1)[-1]}\n\n"
        try: await editable.edit(text, disable_web_page_preview=True)
        except MessageNotModified: pass


async def run():
    await vivdiskBot.start()
    print("\n\nBot Started!\n\n")
    await idle()
    await vivdiskBot.stop()
    print("\n\nBot Stopped!\n\n")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(run())
