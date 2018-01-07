"""
Created by Bartosz Kosakowski
01/07/2018 (mm/dd/yyyy)
A discord bot used to get the weather by typing !weather <city> into
the chat window.
"""
from weather import Weather;
import random;
import discord;

client = discord.Client();

@client.event
async def on_ready():
    print('Logged in as');
    print(client.user.name);
    print(client.user.id);
    print('------');

@client.event
async def on_message(message):
	if message.content.startswith("!weather"):
		print("fuk u");

#reads in the secret token for the bot to log in with
f = open("bottoken.txt","r");
secret = f.read();
f.close();

client.run(secret);