from operator import truediv

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content=True
intents.members=True


bot = commands.Bot(command_prefix='Hello',intents=intents)

enter_role ="Human"

@bot.event
async def on_ready():
    print(f"We are ready to go in, {bot.user.name}")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome {member.mention} read the rules have fun!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "test" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - Don't use that word!")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")



@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Human")
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} is now assigned {role.mention}!")
    else:
        await ctx.send("Role doesn't exist!")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
