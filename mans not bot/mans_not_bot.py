"""
Big Shaq
Created by Bartosz Kosakowski

The ting go skrraaaaaaat
Idea credit goes to me, Joachim, and Peter
"""

#important link for personal reference https://discordapp.com/oauth2/authorize?&client_id=[CLIENT_ID]&scope=bot&permissions=0
#[CLIENT_ID] is supposed to be whatever code is on the dev page.
import discord;
import asyncio;
import youtube_dl;
from random import randint;

#=-=-=Globals and whatnot=-=-=
client = discord.Client();
mans_not_hot = "https://www.youtube.com/watch?v=KZgjdQwuUb8";

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
	#If the user calls the bot with !datinggo then it types out the main lyrics
	if message.content.startswith("!datinggo"):
		await client.send_message(message.channel, "Da ting go skkkkrrrraaa, papakakaka. Skivipipopop and a poopooturrrboom Skrra, tutukukututoom, poompoom. You dun know.");
	
	#If the user calls the bot with !quickmaffs it does some quick maffs
	if message.content.startswith("!quickmaffs"):
		num1 = randint(0,101);
		num2 = randint(0,101);
		sum = num1 + num2;
		await client.send_message(message.channel, str(num1) + " PLUS " + str(num2) + " IS " + str(sum) + " QUICK MAFFS");

	#If the user types !ting it posts a link to the meme 
	if message.content.startswith("!ting"):
		await client.send_message(message.channel, mans_not_hot);
	
	#If the user types !bigshaqirl then the bot joins the channel and plays DA TING GOES
	if message.content.startswith("!bigshaqirl"):
		voice = await client.join_voice_channel(channel);
		player = await voice.create_ytdl_player(mans_not_hot);
		player.start();
		# author = message.author;
		# voice_channel = author.voice_channel;
		# vc = await client.join_voice_channel(voice_channel);
		# player = await vc.create_ytdl_player(mans_not_hot);
		# player.start();
		await client.send_message(message.channel, "This part is not yet implemented");
	
	#Type @Mans Not Bot to get a quick blurb of info about the bot
	if message.content.startswith("<@371525221921980436>"):
		await client.send_message(message.channel, "Created by Bartosz Kosakowski. Okay. Aight. Boom. Type !datinggo, !quickmaffs, !ting, or !bigshaqirl");

# @client.command(pass_context=True)
# async def yt(ctx, url):

#     author = ctx.message.author
#     voice_channel = author.voice_channel
#     vc = await client.join_voice_channel(voice_channel)

#     player = await vc.create_ytdl_player(url)
#     player.start()

client.run('SECRET');