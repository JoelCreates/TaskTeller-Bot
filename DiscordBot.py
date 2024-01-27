#!/usr/bin/python3

import time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import datetime
from datetime import date
import schedule
import discord
import random
import sys
import requests
import json
import asyncio
import aiocron
import youtube_dl
import os
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''

#Token
Token = 'Your-Discord-Bot-Token'

intents = discord.Intents.default()
#intents.members = True
intents.message_content = True
allowed_mentions = discord.AllowedMentions(roles = True)

#Other Bot Configurations
description = '''Discord Bot Description'''
bot = commands.Bot(command_prefix='?', description=description, intents=intents)
client = bot
queues = {}
players = {}



async def hwreminder():
    c = bot.get_channel(Your-Channel-ID)
    await c.send("@everyone Reminder that the study session is HH:MM today! Don't miss X-Subject before you regret it in the exams :/")

# Examples of what different reminder functions looks like
"""
async def ghanavsuruguay():
    c = bot.get_channel(Specific-Discord-Channel-ID)
    await c.send("@everyone Reminder to cheer for Ghana!")


async def reminder2():
    c = bot.get_channel(Your-Channel-ID)
    await c.send("<@&Specific-Role-ID> Reminder that the study session is at HH:MM today!")

async def hwremindernetsec():
    c = bot.get_channel(Your-Channel-ID)
    await c.send("<@&Specific-Role-ID> Reminder that the study session is at HH:MM today!")
"""   

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    
    scheduler = AsyncIOScheduler()

    #Schedulers, can add "jobs" to them with specific arguments acting as configuration edits, triggering specific functions (hwreminder in this case, which was defined earlier) along with the time it will be triggered.
    #The day of the week has to be in three letters.
    scheduler.add_job(hwreminder, CronTrigger(day_of_week="DAY", hour="10", minute="00", second="00"))


    #Starting the Scheduler
    scheduler.start()



@bot.event
async def on_member_join(member):
    channel = bot.get_channel(Specific-Discord-Channel-ID) #Use whichever channel ID you intend to execute this greeting function.
    await channel.send("@" + str(member) + " Hi! Welcome to the server!")
    
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(Specific-Discord-Channel-ID)
    await channel.send("Goodbye "+ str(member))
   

@bot.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You must be in a voice channel run this command!")
        
@bot.command(pass_context = True)
async def play(ctx, url:str):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }]
         }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            
        for file in os.listdir("./"):
            if file.endswith("mp3"):
                os.rename(file, "song.mp3")
                
        source = FFmpegPCMAudio('song.mp3')
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))
    else:
        await ctx.send("You must be in a voice channel run this command!")
        
@bot.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("There is no audio playing at the moment!")
        
@bot.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("There is no audio paused at the moment!")
        
@bot.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()
       
@bot.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I have departed from the channel sire!")
    else:
        await ctx.send("You are not in a voice channel!")
        
# Joke function, this is currently a work in progress        
"""   
@bot.command()
async def joke(ctx):
    jokeurl = "https://joke3.p.rapidapi.com/v1/joke"
    headers = {'x-rapidapi-key': "38498ed9a8mshfd5bd320d9467b9p1cde4djsnfe4154fdb07f",'x-rapidapi-host': "joke3.p.rapidapi.com"}
    response = requests.request("GET", jokeurl, headers=headers)
    print(response.text)
"""

@bot.command()
async def hello(ctx):
    #Random Responses
    value = random.randint(1,9)
    message = ""
    if value <= 4:
        message = "Hey!"
    elif value == 5:
        message = "Greetings"
    elif value >= 6 <= 8:
        message = "Love you man"
    elif value == 9:
        message = "Nah I'd Win"
    await ctx.send(message)

    
@bot.command()
async def faq(ctx):
    await ctx.send("""1. How do I play music? \n
Use the command '?play youtubeurl' in order to play music, at the moment it only works with music on Youtube""")
    
@bot.command()
async def mute(ctx):
    await ctx.send("User has been muted")
    
@bot.command()
async def unmute(ctx):
    await ctx.send("User has been unmuted")
    
@bot.command()
async def members(ctx):
    await ctx.send("Current members for this role are as listed:\n")
    

@bot.command()
#@commands.has_role("The Admin")
async def addrole(ctx, member: discord.Member, role: discord.Role):
    if ctx.author.guild_permissions.administrator:
        # member = member or ctx.author
        await member.add_roles(role)
        await ctx.send(f"The role ''**{role}**'' was just given to you")
#await member.add_roles(role)
    
@bot.command()
async def remrole(ctx):
    await ctx.send("Role has been deleted!")
  
bot.run(Token)
