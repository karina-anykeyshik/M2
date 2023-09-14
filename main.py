import requests
import discord
from discord.ext import commands
import os, random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def mem(ctx):
    image_name = random.choice(os.listdir('images'))
    with open(f'images/{image_name}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)



@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
@bot.command()
async def flip_coin(ctx):
    flip = random.randint(0, 2)
    if flip == 0:
        await ctx.send('ОРЁЛ')
    else:
        await ctx.send('РЕШКА')

bot.run('MTE0MTU5Nzk5MTk5Njc1NjA0MA.Gi1N92.TeZ378v7I7gXkxJ-LtGIf_eCzeSVrJAQvM7byc')
