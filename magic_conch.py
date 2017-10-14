"""
Multi-Purpose discord bot
Created by Bartosz Kosakowski

A multi-purpose bot that initially started out as a Magic Conch bot
Magic Conch idea goes to my friend Caroline
"""

#important link for personal reference https://discordapp.com/oauth2/authorize?&client_id=[CLIENT_ID]&scope=bot&permissions=0
#[CLIENT_ID] is supposed to be whatever code is on the dev page
import discord;
import asyncio;
import pickle;
import os;
import datetime;
from random import *;

#Global vars and whatnot
client = discord.Client();
answers = ["yes", "no", "absolutely", "definitely not", "probably", "probably not", "maybe", "maybe some day", "I don't know", "Not in a million years", "why are you asking me?"];

votetopic = ""
polDict = {};

@client.event
async def on_ready():
    print('Logged in as');
    print(client.user.name);
    print(client.user.id);
    print('------');

@client.event
async def on_message(message):
	"""
	=-=-= MAGIC CONCH BOT =-=-=
	Once the bot is on the discord server, ask it a question by 
	calling !conch, <question>". It will provide respond
	with "yes", "no", "probably", "probably not", "maybe", or 
	"maybe some day" and other stuff maybe.
	"""
	if message.content.startswith("!conch"):
		conch_answer = sample(answers, 1);
		await client.send_message(message.channel, ":shell: " + str(conch_answer));

	#Type !whomst to get a quick blurb of info about the bot
	if message.content.startswith("!whomst"):
		await client.send_message(message.channel, "A multi-purpose bot created by Bartosz Kosakowski. It initially started off as a Magic Conch bot, now does a whole bunch of other things! Type !cmdhelp");

	#Type !cmdhelp into the chat to get a list of commands
	if message.content.startswith("!cmdhelp"):
		await client.send_message(message.channel, 
			"""\n
			----COMMANDS LIST----\n
			General:\n
			\t!whomst - if you want to more about the bot\n
			Magic Conch:\n
			\t!conch <question> - ask the magic conch a question\n
			Big Ben:\n
			\t!bigben - gives the current hour in BONGS\n
			Quotes:\n
			\t WORK IN PROGRESS, DOES NOT WORK\n
			\t!quote <quote> - did someone say something dumb? Immortalize it!\n
			\t!randquote - pulls a random quote that was added\n
			Rock the vote:\n
			\t WORK IN PROGRESS, DOES NOT WORK\n
			\t!votetopic <topic> - add a topic to vote on\n
			\t!addoption <option> - adds a voting option\n
			\t!voteoption <option> - vote for an option\n
			\t!showres - shows poll results""");

	#BIG BEN
	#Prints the time in BONGS (and BINGS?)
	if message.content.startswith("!bigben"):
		hours = "";
		int_time = int("%s" % (datetime.datetime.now().hour));
		for i in range(int_time):
			hours += " BONG";
		await client.send_message(message.channel, ":clock:" + hours);

	#ROCK THE VOTE
	#Cast a vote on whatever user specified items
	if message.content.startswith("!votetopic"):
		global votetopic
		votetopic = (message.content[11:]);
		await client.send_message(message.channel, votetopic + " ");
	#Adds a poll option
	if message.content.startswith("!addoption"):
		print(votetopic);
		if not votetopic:
			await client.send_message(message.channel, "Please enter a vote topic first with !votetopic");

client.run('MzY4MjgwNzA1MzgzMzk5NDI0.DMJyoQ.dnm19X8QZ7Ibl_5RD-a1cAQT9Ms');