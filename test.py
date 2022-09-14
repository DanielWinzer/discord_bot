import os, discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

prefix_command="!!"

intents = discord.Intents.all()

client = commands.Bot(command_prefix=prefix_command,intents=intents)


#login and set activity
@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))
	activity = discord.Game(name=prefix_command + "ping")
	await client.change_presence(status=discord.Status.online,activity=activity)

@client.command(pass_context=True)
async def ping(ctx):
	await ctx.send(f"Ping: {client.latency}")

@client.event
async def on_message(message):
  if message.content.find("tiktok.com",0,len(message.content))!=-1:
    await message.delete()
    await message.channel.send("NO TIKTOK")

my_secret = os.environ['DISCORD_TOKEN']
client.run(my_secret)