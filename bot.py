"""A bot for discord. Needs python3.6

To add bot:

    https://discord.com/oauth2/authorize?client_id=776331747402711051&scope=bot&permissions=2080
"""
import os
import random
import sys

import dotenv

import discord
from discord.ext import commands

dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")

CIVILIZATIONS = {
    'British': ':flag_gb:',
    'Dutch': ':flag_nl:',
    'French': ':flag_fr:',
    'Germans': ':flag_de:',
    'Ottomans': ':flag_tr:',
    'Portuguese': ':flag_pt:',
    'Russians': ':flag_rs:',
    'Spanish': ':flag_es:',
    'Aztecs': ':flag_mx:',
    'Haudenosaunee': ':flag_us:',
    'Lakota': ':flag_re:',
    'Chinese': ':flag_cn:',
    'Indians': ':flag_in:',
    'Japanese': ':flag_jp:',
}

if not TOKEN:
    print("No token set")
    sys.exit(1)


intents = discord.Intents(messages=True, members=True, guilds=True)
bot = commands.Bot(command_prefix='--', intents=intents)


@bot.command(name="hello")
async def on_message(ctx):
    msg = f'Hello {ctx.author.mention}'
    await ctx.send(msg)


@bot.command(name="shuffle")
async def on_shuffle(ctx):
    civilizations = list(CIVILIZATIONS.keys())
    random.shuffle(civilizations)
    result = ["The random civilizations:"]
    i = 0
    for member in ctx.guild.members:
        if member.bot:
            continue
        civ = civilizations[i]
        i += 1
        result.append(f"{member.mention}, Civilization: {civ}   {CIVILIZATIONS[civ]}")
    await ctx.send("\n".join(result))


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.run(TOKEN)
