from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

# -----Создаем клавиатуру с помощью ReplyKeyboardBuilder-----

button_yes = KeyboardButton(text=LEXICON_RU['yes_button'])
button_no = KeyboardButton(text=LEXICON_RU['no_button'])

yes_no_kb_builder = ReplyKeyboardBuilder()

yes_no_kb_builder.row(button_yes, button_no)

yes_no_kb: ReplyKeyboardMarkup = yes_no_kb_builder.as_markup(
    one_time_keyboard=True,
    resize_keyboard=True
)

# -----Создаем rock_papper_scissors клаву без использования билдера-----

button_1 = KeyboardButton(text=LEXICON_RU['rock'])
button_2 = KeyboardButton(text=LEXICON_RU['paper'])
button_3 = KeyboardButton(text=LEXICON_RU['scissors'])

# Создаем игровую клавиатуру с кнопками "Камень 🗿",
# "Ножницы ✂" и "Бумага 📜" как список списков
game_keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1],
              [button_2],
              [button_3]],
    resize_keyboard=True
)