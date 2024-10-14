from aiogram import types

from filters import IsGroup
from loader import dp, bot
import re

@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(message: types.Message):
    members = ", ".join([m.get_mention(as_html=True) for m in message.new_chat_members])
    await message.reply(f"Xush kelibsiz, {members}.")


@dp.message_handler(IsGroup(), content_types=types.ContentType.LEFT_CHAT_MEMBER)
async def banned_member(message: types.Message):
    if message.left_chat_member.id == message.from_user.id:
        await message.answer(f"{message.left_chat_member.get_mention(as_html=True)} guruhni tark etdi")
    elif message.from_user.id == (await bot.me).id:
        return
    else:
        await message.answer(f"{message.left_chat_member.full_name} guruhdan haydaldi "
                             f"Admin: {message.from_user.get_mention(as_html=True)}.")



@dp.message_handler(IsGroup(), content_types=types.ContentType.ANY)
async def delete_links(message: types.Message):
    # Admin tomonidan yuborilgan bo'lsa, o'tkazib yuboramiz
    member = await message.chat.get_member(message.from_user.id)
    if member.is_chat_admin():
        return

    # Linklarni aniqlash uchun takomillashtirilgan regex
    url_pattern = r"(https?://[^\s]+|www\.[^\s]+|t\.me/[^\s]+|@\w+)"

    # Xabardagi matnni tekshirish
    if message.text and re.search(url_pattern, message.text):
        await message.delete()
        await message.answer(f"{message.from_user.full_name}, guruhga reklama yubormang !")
        return

    # Rasm yoki video izohini tekshirish
    if message.caption and re.search(url_pattern, message.caption):
        await message.delete()
        await message.answer(f"{message.from_user.full_name}, guruhga reklama yubormang !")
