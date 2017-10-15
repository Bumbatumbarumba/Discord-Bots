"""
Big Ben
Created by Bartosz Kosakowski

A bot that gives the current hour in BONGS, like Big Ben in England
Idea credit goes to my friend Peter
"""

#important link for personal reference https://discordapp.com/oauth2/authorize?&client_id=[CLIENT_ID]&scope=bot&permissions=0
#[CLIENT_ID] is supposed to be whatever code is on the dev page.
import discord;
import asyncio;
import pickle;
import os;
import datetime;
from random import *;

#=-=-=Global vars and whatnot=-=-=
client = discord.Client();

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
	#If the user calls the bot with !bigben, it reads the computer's current time,
	#converts it to 12 hour format, and prints the hour in BONGS 
	if message.content.startswith("!bigben"):
		hours = "";
		int_time = int("%s" % (datetime.datetime.now().hour));
		if int_time > 12:
			int_time = int_time-12;
			
		for i in range(int_time):
			hours += " BONG";
		await client.send_message(message.channel, ":clock:" + hours);

	#Type @Magic Conch to get a quick blurb of info about the bot
	if message.content.startswith("<@369196453702270976>"):
		await client.send_message(message.channel, "Created by Bartosz Kosakowski. Type !bigben to get the current time in BONGS");

client.run('MzY5MTk2NDUzNzAyMjcwOTc2.DMVAjw.Qjxbp9T3AyhE5O6jpWxWrjwjO3w');