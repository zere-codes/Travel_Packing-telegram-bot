import asyncio
from aiogram.filters import *
from aiogram import *
from aiogram.types import *
import logging
from dotenv import load_dotenv
import os
from dataclasses import dataclass
from weather_get import get_weather
from package_recommend import luggage_list
from city_photo import get_city_photo
load_dotenv()
@dataclass(frozen=True)

class Config:
    token: str
def load_config() -> Config:
    token = (os.getenv("BOT_TOKEN"))
    if not token:
        raise RuntimeError("BOT_TOKEN не найден. Создай .env и добавь BOT_TOKEN=...")
    return Config(token=token)

config=load_config()
WEATHER_KEY = os.getenv("WEATHER_KEY")
bot=Bot(token=config.token)
dp=Dispatcher()
logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Я бот-помощник для подготовки к путешествию. Я рекомендую, какие вещи обязательно взять с собой, в зависимости от города и длительности поездки.")
@dp.message(Command("pack"))
async def pack(message:Message,command:CommandObject):
    if not command.args:
        await message.answer("Ошибка. Введите название города и продолжительность(в днях). Пример: Алматы 5")
    else:
        args = command.args.split()
        if len(args) != 2:
            await message.answer("Пожалуйста введите название города И продолжительность ")
        else:
            city = args[0]
            dates= args[1]
            if dates.isdigit()==False:
                await message.answer("Ошибка:  введите продолжительность в числах.Пример: Алматы 5")

            else:
                 dates = int(args[1])
                 weather_info=get_weather(city)
                 if weather_info:
                     temp, weather=weather_info
                 else:
                     await message.answer(f"Не удалость получить данные о погоде в городе {city}")

                 luggage_info=luggage_list(temp,weather, dates)
                 if luggage_info:
                     luggage=luggage_info
                 else:
                     await message.answer(f"Не удалость получить список вещей")
                 photo_url = get_city_photo(city)

                 if luggage_info and weather_info:
                     recommend = (
                         f"🌡️Температура в {city}: {temp} градусов\n"
                         f"🛰️Погода: {weather}\n"
                         f"🧳Рекомендуемые вещи:\n {luggage}\n"

                     )
                     if photo_url:
                         await message.answer_photo(photo_url, caption=recommend)
                     else:
                         await message.answer("Ошибка с загрузкой фото")


                         await message.answer(recommend)









@dp.message(Command("help"))
async def help(message:Message):
    await message.answer("Доступные команды:"
                         "\n/start - начать работу с ботом"
                         "\n/help - получить список доступных команд"
                         "\n/pack - получить рекоммендации по подготовке к путешествию")
@dp.message()
async def empty(message:Message):
    await message.answer("Я не понимаю. Напишите /help")







async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())