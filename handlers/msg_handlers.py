import requests
from aiogram import Router
import re
from aiogram.enums import ParseMode
from  aiogram.types import Message
from config import courses

from forex_python.converter import CurrencyRates
import logging
from datetime import datetime,timedelta



msg_router=Router()

@msg_router.message()
async def convert_sum(message:Message):
    try:
       x=int(message.text)
       s=f"{x} so'm \n"
       s+=f"\t -{x/courses['USD']: .2f} dollor\n"
       s+=f"\t -{x/courses['EUR']: .2f} yevro\n"
       s+=f"\t -{x/courses['RUB']: .2f} rubl\n"
       await message.reply(text=s)
    except:
        await message.reply("Iltimos faqat son kiriting:")




@msg_router.message()
async def convert_dol(message:Message):
    x=str(message.text)
    if "dollor" or "$" in x:
        a= [int(s) for s in x.split() if s.isdigit()]
        if a:
            x1= a[0]
            s=f"{x1*courses['USD']: .2f} so'm"
    elif "yevro" or "€" in x:
        a = [int(s) for s in x.split() if s.isdigit()]
        if a:
            x1 = a[0]
            s = f"{x1 * courses['EUR']: .2f} so'm"
    elif "rubl" or "₱" in x:
        a = [int(s) for s in x.split() if s.isdigit()]
        if a:
            x1 = a[0]
            s = f"\t -{x1*courses['RUB']: .2f} so'm\n"
    await message.reply(text=s)



@msg_router.message()
async def convert_sum(message: Message):
    if message. text.count("-") == 2:
        x = str(message.text)
        x_index = str(x).index("-")
        sana = x[x_index - 4: x_index + 6]
        if x_index > 5:
            matn = x[:x_index - 5]
        else:
            matn = x[x_index + 7:]

        if matn=="USD" or matn=="dollar" :
            matn = "USD"
            response = requests.get(f"https://cbu.uz/oz/arkhiv-kursov-valyut/json/{matn}/{sana}/")
            for kurs in response.json():
                s =f"{sana}\n{kurs['Rate']}"
            await message.reply(text=s)

        elif matn=="EUR" or matn=="yevro":
            matn="EUR"
            response = requests.get(f"https://cbu.uz/oz/arkhiv-kursov-valyut/json/{matn}/{sana}/")
            for kurs in response.json():
                s = f"{sana}\n{kurs['Rate']}"
            await message.reply(text=s)

        elif matn=="RUB" or matn=="rubl":
            matn = "RUB"
            response = requests.get(f"https://cbu.uz/oz/arkhiv-kursov-valyut/json/{matn}/{sana}/")
            for kurs in response.json():
                s = f"{sana}\n{kurs['Rate']}"
            await message.reply(text=s)
        else:
            await message.reply(text=f"Siz noto'g'ri matn kiritdingiz:(Iltimos USD, dollar; EUR,yevro; RUB,rubl dan birini kiriting.)")

