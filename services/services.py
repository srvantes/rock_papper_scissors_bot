import random
from lexicon.lexicon import LEXICON_RU

# пик бота
def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])

# Функция, возвращающая ключ из словаря, по которому
# хранится значение, передаваемое как аргумент - выбор пользователя
def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if user_answer == LEXICON_RU[key]:
            break
    return key

# функция определяющая победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'