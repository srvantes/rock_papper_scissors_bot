from environs import Env
from dataclasses import dataclass

# создаем класс бота
@dataclass
class TgBot:
    token: str # Токен для доступа к боту

@dataclass
class Config:
    tg_bot: TgBot

def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env()
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))