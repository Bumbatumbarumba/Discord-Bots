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
	print("eeeee");

client.run('SECRET');