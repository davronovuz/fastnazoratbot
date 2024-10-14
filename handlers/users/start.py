from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate

from loader import dp, db
import logging


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    try:
        username = message.from_user.username if message.from_user.username else "Ism yo'q"
        user_id = message.from_user.id

        # Foydalanuvchi bazada bor-yo'qligini tekshirish
        if not db.select_user(telegram_id=user_id):
            db.add_user(telegram_id=user_id, username=username)

        # Start xabar
        start_message = """
        Salom! Men  🤖 <b> Fast Nazorat Botman </b>, guruhingizni nazorat qilish uchun tayyor turibman. Quyida mening asosiy vazifalarim bilan tanishing:

        - **Yangi A'zolarni Kutib Olish:** Guruhga yangi qo'shilgan a'zolarni avtomatik ravishda kutib olaman va ularga guruh qoidalari haqida ma'lumot beraman.

        - **Guruh Qoidalarini Boshqarish:** Guruhingiz uchun qoidalar o'rnatishingiz mumkin, men esa bu qoidalarni kuzatib, buzilgan taqdirda tegishli choralar ko'raman.

        - **Spam va Noo'rin Kontentni Filtrlash:** Guruhda spam yoki noo'rin kontent paydo bo'lsa, uni avtomatik ravishda o'chiraman va kerak bo'lsa, foydalanuvchini ogohlantiraman.

        - **Foydalanuvchi Faolligini Kuzatish:** Guruh a'zolarining faolligini kuzatib, statistik ma'lumotlarni taqdim etaman.

        - **Maxsus Buyruqlarni Qabul Qilish:** Sizning ehtiyojlaringizga mos maxsus buyruqlarni yaratib, ularga javob bera olaman.

        - **Guruh Ma'lumotlarini O'zgartirish:** Guruh nomi, rasmi, tavsifi (description) kabi ma'lumotlarni o'zgartirish imkoniyatiga egaman. Guruhingizni yanada moslashtirish uchun buyruqlarim orqali buni amalga oshirishingiz mumkin.

        - **A'zolarni Mute va Ban Qilish:** Guruhda noo'rin xatti-harakat qilgan a'zolarni vaqtincha sukutga olish (mute) yoki guruhdan chetlatish (ban) funksiyasiga egaman.

        - **Men faol ishlashim uchun meni guruhga qo'shib admin qiling.**
        """
        await message.answer(start_message, parse_mode="HTML")

    except Exception as e:
        logging.error(f"Xato yuz berdi: {e}")
