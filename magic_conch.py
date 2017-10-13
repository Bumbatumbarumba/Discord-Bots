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
		await client.send_message(message.channel, ":shell: " + str(conch_answer));

	if message.content.startswith("!cmdhelp"):
		await client.send_message(message.channel, """----COMMANDS LIST----\n
			General:\n
			\t!whomst - if you want to more about the bot\n
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

client.run('MzY4MjgwNzA1MzgzMzk5NDI0.DMJyoQ.dnm19X8QZ7Ibl_5RD-a1cAQT9Ms');