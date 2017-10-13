"""
Magic conch discord bot
Created by Bartosz Kosakowski
Idea credit goes to my friend Caroline 

Once the bot is on the discord server, ask it a question by 
calling "!magic_conch, <question>". It will provide respond
with "yes", "no", "probably", "probably not", "maybe", or 
"maybe some day" and other bs.
"""

import discord;
import asyncio;
from random import *;

client = discord.Client();
answers = ["yes", "no", "probably", "probably not", "maybe", "maybe some day", "I don't know", "Not in a million years", "why are you asking me?"];

@client.event
async def on_ready():
    print('Logged in as');
    print(client.user.name);
    print(client.user.id);
    print('------');

@client.event
async def on_message(message):
	if message.content.startswith("!conch"):
		conch_answer = sample(answers, 1);
		await client.send_message(message.channel, "\:shell:" + str(conch_answer));

	if message.content.startswith("!cmdhelp"):
		await client.send_message(message.channel, "Commands: !conch");

client.run('MzY4MjgwNzA1MzgzMzk5NDI0.DMJyoQ.dnm19X8QZ7Ibl_5RD-a1cAQT9Ms');