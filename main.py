import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import os
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command(help="Play with .rps [your choice]")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"Какой твой выбор?")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = await bot.wait_for('message', check=check)

    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Nice try, but I won that time!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.send(f'The pen beats the sword? More like the paper beats the rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Oh, wacky. We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Aw man, you actually managed to beat me.\nYour choice: {user_choice}\nMy choice: {comp_choice}")

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.send(f'HAHA!! I JUST CRUSHED YOU!! I rock!!\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'paper':
            await ctx.send(f'Bruh. >: |\nYour choice: {user_choice}\nMy choice: {comp_choice}')
        elif comp_choice == 'scissors':
            await ctx.send(f"Oh well, we tied.\nYour choice: {user_choice}\nMy choice: {comp_choice}")
@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animal(ctx):
    images = os.listdir('animal')
    img_name = random.choice(images)
    with open(f'animal/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def reklama(ctx):
    images = os.listdir('reklam')
    img_name = random.choice(images)
    with open(f'reklam/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def ecology(ctx):
    images = os.listdir('ecology')
    img_name = random.choice(images)
    with open(f'ecology/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("token")