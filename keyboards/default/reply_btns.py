from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def start_btn():
    btn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    btn.add(KeyboardButton('🎧 All Music'), KeyboardButton('🏆 Top Music'),
            KeyboardButton('🆕 New Music'), KeyboardButton('🎵 Tik-Tok Music'))
    return btn


def admin_page():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    markup.add(KeyboardButton('📊 Statistika'), KeyboardButton('🔔 Reklama'), KeyboardButton('🔙 Back'))
    return markup






def admin_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    statistika = KeyboardButton("statistika📊")
    reklama = KeyboardButton("Reklama 🎁")
    add_chanell = KeyboardButton("Kanallar 🖇")
    return btn.add(statistika, reklama, add_chanell)




def channels_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
    add_channel = KeyboardButton("Kanal qo'shish ⚙️")
    delete_channel = KeyboardButton("Kanal o'chirish 🗑")
    exits = KeyboardButton("❌")
    return btn.add(add_channel, delete_channel, exits)


def exit_btn():
    btn = ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2, resize_keyboard=True)
    return btn.add("❌")