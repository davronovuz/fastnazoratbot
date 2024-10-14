from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("stats", "Guruhda eng ko'p yozgan foydalanuvchilar "),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("ban", "Foydalanuvchini guruhdan haydash"),
            types.BotCommand("unban", "Foydalanuvchini guruhga qayta qo'shish"),
            types.BotCommand("ro", "Foydalanuvchini guruhda yozishini cheklash"),
            types.BotCommand("unro", "Foydalanuvchini yozishga ruxsat berish"),
            types.BotCommand("mute_all", "Barcha foydalanuvcchilarni yozishini cheklash "),
            types.BotCommand("set_photo", "Guruh rasmini o'zgartirish"),
            types.BotCommand("set_title", "Guruh nomini almashtirish"),
            types.BotCommand("set_description", "Guruh ma'lumotini almashirish"),
        ]
    )
