"""
Multi-Purpose discord bot
Created by Bartosz Kosakowski

A multi-purpose bot that initially started out as a Magic Conch bot
Magic Conch idea goes to my friend Caroline
"""

import discord;
import asyncio;
import pickle;
import os;
import datetime;
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

	#Type !cmdhelp into the chat to get a list of commands
	if message.content.startswith("!cmdhelp"):
		await client.send_message(message.channel, """
			----COMMANDS LIST----\n
			General:\n
			\t!whomst - if you want to more about the bot\n
			Big Ben:\n
			\t!bigben - gives the current hour in BONGS 
			Magic Conch:\n
			\t!conch <question> - ask the magic conch a question\n
			Gucci Points:\n
			\t WORK IN PROGRESS, DOES NOT WORK\n
			\t!gpwhatis - explains what Gucci Points are\n
			\t!gpadd <user> - add a user that can receive Gucci Points\n
			\t!gpgive <user> <integer> - give a user Gucci Points\n
			\t!gprank - lists all users by Gucci Points\n
			\t!gplist - lists all users who can gain Gucci Points\n
			Quotes:\n
			\t WORK IN PROGRESS, DOES NOT WORK\n
			\t!quote <quote> - did someone say something dumb? Immortalize it!\n
			\t!randquote - pulls a random quote that was added""");

	if message.content.startswith("!whomst"):
		await client.send_message(message.channel, """
			A multi-purpose bot created by Bartosz Kosakowski\n
			Initially started off as a Magic Conch bot, now does\n
			a whole bunch of other things! Type !cmdhelp""");

	"""
	=-=-= GUCCI POINTS =-=-=
	Give a user Gucci Points for whatever reason you want
	"""
	if message.content.startswith("!gpwhatis"):
		await client.send_message(message.channel, "Did someone do something cool? Give them Gucci Points!\nDid they do something dumb? Take them away!");
	# if message.content.startswith("!gpadd"):
	# 	await client.send_message(message.channel, )

	#BIG BEN
	#returns the time in BONGS (and BINGS?)
	if message.content.startswith("!bigben"):
		now = datetime.datetime.now();
		hours = "";
		for i in range(now.hour):
			hours += " BONG";
		await client.send_message(message.channel, ":clock:" + hours);

client.run('MzY4MjgwNzA1MzgzMzk5NDI0.DMJyoQ.dnm19X8QZ7Ibl_5RD-a1cAQT9Ms');