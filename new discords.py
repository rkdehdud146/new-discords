import discord
import os


client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.id)
    print("ready")
    print('------')
    game =discord.Game
    await client.change_presence(status=discord.Status.online, activity=game)


@client.even
async def on_message(massage):")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
