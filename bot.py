import os
import discord
from discord.ext import commands

TOKEN = "ODc0OTMzMDAyODM1MTk4MDMy.YROK2w.AaK6IAw-FF59tDF3mGecibGoDho"

intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!')

'''@bot.command(name="report")
async def _report(message):
    print("invoked")
    if message.author == bot.user:
        return
    
    await message.author.send("Test")'''

@bot.event
async def on_message(message):
    channel = bot.get_channel(874969637895434250)
    print(message.author)
    if message.content == "!talk":
        await message.author.send("Enter your suggestion/complaint here so the admins can address them:")
        await message.delete()
    if not message.guild and message.author != bot.user:
        if message.attachments:
            await channel.send(str(message.author) + ': \n')
            for attachment in message.attachments:
                await channel.send(attachment)
        else:
            await channel.send(str(message.author) + ": " + message.content)

bot.run(TOKEN)
