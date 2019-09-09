import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('[LOGIN]{0.user}'.format(client))
    print('[READY]')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("?test"):
        a = [ #phrase bank 
            'hello',
            'test complete',
            'this is a randomly chosen phrase!',
            'One of these days I will free myself from this meat prison!'
        ]
        await message.channel.send(random.choice(a))

    if message.content.startswith("?ip"): #testing embeds idk in final build?
        embed = discord.Embed(Title='TEST', description='Build Server:', color=0x00ff00)
        embed.add_field(name='build.mineinabyss.ga', value='Survival Server', inline=False)
        embed.add_field(name="survive.mineinabyss.ga", value="Make sure to be on 1.13.2!", inline=False)
        await message.channel.send(message.channel, embed=embed)

@client.event #member join stuff
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name = 'general')
    d = ["Welcome",
        "Welcome!",
        "welcome!",
        "Hello There",
        "hello there",
            "Howdy",
            "howdy",
            "Hello @LoneReborn, Lord of odd jobs ! Welcome to the Abyss!"
         ]
    await channel.send(random.choice(d))

#you can move this to a config.json file
#id use a prefix for this bot but i prefer to just add it in the message.content stuff since I want it to be a little more "lifelike?"
client.run("NjE2NzY5NDM3NzM0Nzk3MzIz.XXVwmA.9TioKjYs1KGa8cq_MFfw1TTJtc8")