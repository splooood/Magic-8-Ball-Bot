# Magic 9 Ball Bot!
# Made by Splode.

import discord
import random
import os
from keep_alive import keep_alive

client = client = discord.Client()

ball = [
  "As I see it, yes.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "It is certain.", "It is decidedly so.", "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", "Yes.", "Yes, definitely.", "You may rely on it."
]

ballagree = [
  "Yes", "Yes, very.", "As I see it, yes.", "It is certain.", "Without a doubt.", "Outlook good.", "Yes, definitely.", "You may rely on it.", "It is decidedly so.", "Most likely.", "Signs point to yes"
]

ballhatred = [
  "Don't count on it.", " My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."
]


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name="8-Ball answers."))
  print('{0.user} is ready to reply.'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content


  if msg.startswith('?help'):
    embed=discord.Embed(title="Help", description="Hi, I am 9-ball. Ask me a question with !9ball (question). I will agree with you always.", color=0xff6961)
    await message.channel.send(embed=embed)

  if msg.startswith('?9ball'):
    embed=discord.Embed(title="I agree.", description=(random.choice(ballagree)), color=0xff6961)
    await message.channel.send(embed=embed)


keep_alive()
client.run("ODMxNTIwNTMwMzIyNTU0ODgw.YHWb1w.qpI-F0Ywhx8fqA_o3Drwszz_py0")

