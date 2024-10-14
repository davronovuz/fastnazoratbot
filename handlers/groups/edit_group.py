import io
from aiogram import types
from aiogram.dispatcher.filters import Command
import re
from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot








# Guruhning rasmini o'zgartirish
@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message

    # Reply xabarni tekshirish va photo borligini aniqlash
    if source_message and source_message.photo:
        photo = source_message.photo[-1]
        photo = await photo.download(destination=io.BytesIO())
        input_file = types.InputFile(photo)
        # Guruh rasmini o'zgartirish
        await message.chat.set_photo(photo=input_file)
        await message.reply("Guruh rasmi muvaffaqiyatli o'zgartirildi.")
    else:
        await message.reply("Iltimos, yangi guruh rasmini reply qiling.")


# Guruh nomini o'zgartirish
@dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message

    # Reply qilingan xabarda yangi nom borligini tekshirish
    if source_message and source_message.text:
        title = source_message.text
        await bot.set_chat_title(message.chat.id, title=title)
        await message.reply(f"Guruh nomi {title} ga o'zgartirildi.")
    else:
        await message.reply("Iltimos, yangi guruh nomini reply qiling.")


# Guruh ma'lumotini (description) o'zgartirish
@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message

    # Reply qilingan xabarda yangi description borligini tekshirish
    if source_message and source_message.text:
        description = source_message.text
        await message.chat.set_description(description=description)
        await message.reply("Guruh ma'lumoti muvaffaqiyatli o'zgartirildi.")
    else:
        await message.reply("Iltimos, yangi guruh ma'lumotini reply qiling.")
