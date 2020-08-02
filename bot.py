import discord
from discord.utils import get
import asyncio
import os
import random

randNum = random.random()
bot = discord.Client()

#Activity

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Republic of United Members"))
    print("Bot is online. Instance ID is " + str(randNum))

#Bot commands
def getLine(fileName,lineNum):
    lines=[]
    fh=open(fileName)
    for i, row in enumerate(): 
        if i+1==lineNum: 
            return row

@bot.event
async def on_message(message):
    if message.channel.id == 737807052625412208:
        await message.add_reaction("✅")
        await message.add_reaction("❌")

#General Commands

    command = message.content.lower()
    if command.startswith('r?test'):
        await message.channel.send(randNum)
    
    if command.startswith('r?info'):
        embedVar = discord.Embed(title="RUM Bot", description="Custom bot developed for the Republic of United Members discord server.", color=0xEC00FF)
        embedVar.add_field(name="Version", value="1.0.1", inline=False)
        embedVar.add_field(name="Contributors:", value="evalyn#8883, pupo#0001", inline=False)
        await message.channel.send(embed=embedVar)
 
    if command.startswith('r?help'):
        embedVar = discord.Embed(title="Help List", description="Command list. Prefix = r? ", color=0xEC00FF)
        embedVar.add_field(name="help", value="Displays this list.", inline=False)
        embedVar.add_field(name="info", value="Displays bot information.", inline=False)
        embedVar.add_field(name="coinflip or cf", value="flip a coin", inline=False)
        await message.channel.send(embed=embedVar)
    if command.startswith('r?coinflip') or command.startswith('r?cf'):
        flipside = bool(random.getrandbits(1))
        if (flipside):
            flipside = "Heads"
        else:
            flipside = "Tails"
        await message.channel.send("The coin landed on " + flipside)

#Rule commands

    if command.startswith('r?rule '):
        ruleNum = int(command.split(" ")[1])
        if 1<=ruleNum<=10:
            embedVar = discord.Embed(title=getLines("rules.txt",2*ruleNum-1), description=getLine("rules.txt",2*ruleNum), color=0xEC00FF)
            await message.channel.send(embed=embedVar)
        else:
            await message.channel.send("Invalid Rule Number")

@bot.event
async def on_raw_reaction_add(payload):
    if payload.channel_id == 737807052625412208:
        if payload.emoji.name == "✅":
            channel = bot.get_channel(737807052625412208)
            message = await channel.fetch_message(payload.message_id)
            reaction = get(message.reactions, emoji=payload.emoji.name)
            if reaction and reaction.count > 5:
                embedVar = discord.Embed(title="✅ Approved", description = message.content , color=0xEC00FF)
                embedVar.add_field(name="Suggested by:", value = message.author.mention, inline=False)
                await bot.get_channel(739172158948900925).send(embed=embedVar)
                await message.delete()
        elif payload.emoji.name == "❌":
            channel = bot.get_channel(737807052625412208)
            message = await channel.fetch_message(payload.message_id)
            reaction = get(message.reactions, emoji=payload.emoji.name)
            if reaction and reaction.count > 5:
                embedVar = discord.Embed(title="❌ Denied", description = message.content , color=0xEC00FF)
                embedVar.add_field(name="Suggested by:", value = message.author.mention, inline=False)
                await bot.get_channel(739172158948900925).send(embed=embedVar)
                await message.delete()



#Bot Token

token = open(os.path.join(os.environ['USERPROFILE'], 'My Documents\\token.txt')).read()
bot.run(token)
