"""
Magic Conch
Created by Bartosz Kosakowski

A bot that behaves like the magic conch from Spongebob Squarepants
Idea credit goes to my friend Caroline
"""

#important link for personal reference https://discordapp.com/oauth2/authorize?&client_id=[CLIENT_ID]&scope=bot&permissions=0
#[CLIENT_ID] is supposed to be whatever code is on the dev page.
import discord;
import asyncio;
import pickle;
import os;
import datetime;
from random import *;

#=-=-=Globals and whatnot=-=-=
client = discord.Client();
#List of answers the bot can choose from; yn_answers applies to any
#questions except ones asking about future events. temporal_answers
#is chosen from if the question asks about future events
yn_answers = ["yes", "no", "absolutely", "definitely not", "probably", "probably not", "maybe", "I don't know"];
temporal_answers = ["yes", "no", "absolutely", "definitely not", "probably", "probably not", "maybe", "maybe some day", "I don't know", "Not in a million years"];

#Logs the bot into the server
@client.event
async def on_ready():
    print('Logged in as');
    print(client.user.name);
    print(client.user.id);
    print('------');

#Checks the message for a specific string (ie, that the bot is being called)
@client.event
async def on_message(message):
	#if the user calls the bot with !chonch, then it randomly picks an answer
	if message.content.startswith("!conch"):
		if message.content[6:] is "" or message.content[6:] is " ":
			await client.send_message(message.channel, ":shell: please ask me a question");
		else:
			if "will" in message.content:
				conch_answer = sample(temporal_answers, 1)
				await client.send_message(message.channel, ":shell: " + str(conch_answer));
			else:
				conch_answer = sample(yn_answers, 1);
				await client.send_message(message.channel, ":shell: " + str(conch_answer));

	#Type @conch to get a quick blurb of info about the bot
	if message.content.startswith("<@368280705383399424>"):
		await client.send_message(message.channel, "Created by Bartosz Kosakowski. Simply emulates the maic conch from Spongebob Squarepants. Type !conch <question>.");

client.run('SECRET');