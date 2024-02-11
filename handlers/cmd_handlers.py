import requests
from aiogram import Router
from aiogram.filters import CommandStart,Command
from aiogram.enums import ParseMode
from  aiogram.types import Message
from config import courses
import logging
import datetime

cmd_router=Router()

@cmd_router.message(CommandStart())
async def cmd_start(message:Message):
    s="Assalomu aleykum!\n Valyutalar kurslari haqida ma'lumot beruvchi botmizga xush kelibsiz!\n Yordam uchum /help buyrug'ini bosing!"
    await message.answer(text=s)

@cmd_router.message(Command("help"))
async def cmd_help(message:Message):
    s="Quydagi komandalar yordamida botdansamarali foydalanishingiz mumkin:\n\n"
    s+="\t/hafta - bir haftalik kurslarni bilish\n"
    s+="\t/kurslar - valyutalar kursini bilish\n"
    s+="\t/dollar - dollar kursini bilish\n"
    s+="\t/yevro - yevro kursini bilish\n"
    s+="\t/rubl - rubl kursini bilish\n"
    s+="Agar biron summani jo'natsangiz bot uni turli valyutalardagi qiymatini qaytaradi. (Masalan,1000000)"
    await message.answer(text=s)


@cmd_router.message(Command("kurslar"))
async def cmd_kurslar(message:Message):
    response=requests.get("https://cbu.uz/oz/arkhiv-kursov-valyut/json/")
    s="Bugungi valyuta kurslari:\n"
    for kurs in response.json():
        if kurs['Ccy'] in ['USD','EUR','RUB']:
            courses[kurs['Ccy']]=float(kurs['Rate'])
            s+=f"1 {kurs['CcyNm_UZ']}-{kurs['Rate']} so'm\n"
    await message.reply(text=s)


@cmd_router.message(Command("hafta"))
async def cmd_hafta(message: Message):
    today = datetime.date.today()
    s = ''
    for i in range(7):
        response = requests.get(f"https://cbu.uz/oz/arkhiv-kursov-valyut/json/all/{today}/")
        s += f"{today}\n"
        for kurs in response.json():
            if kurs["Ccy"] in ["USD", "EUR", "RUB"]:
                s += f"1 {kurs['CcyNm_UZ']} - {kurs['Rate']} so'm\n"
        today = today - datetime.timedelta(days=1)
        s += "\n"
    await message.reply(text=s)