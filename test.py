
import os
import select
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
#client = commands.Bot("!")
@client.event
async def on_ready():
        print(f'{client.user} has connected to Discord!')

@client.event
async def on_closed():
    print('closed')

@client.command()
async def ping(ctx):
	await ctx.channel.send("pong!")

965794132536721418
@client.event 
async def on_message(message):
    print("new message");
    await client.get_channel(965794132536721418).send('test ok read msg ');

client.run(TOKEN)