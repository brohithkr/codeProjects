import discord
from psatt import *
from secret import roll, passwd, sess_token, bot_token
from datetime import datetime
# import os
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
client = discord.Client(intents=intents)
print(client.user)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/psatt'):
        print(message.author,message.content)
        # a,b = map(lambda x: float(x) if '.' in x else int(x),message.content[5:].strip().split())

        # await message.channel.send(f'{a}+{b}={a+b}')
        rollno = message.content.split(" ")[1]
        raw_att = (get_ps_att(roll))
        print(raw_att)
        att = get_formatted(raw_att)
        print(att)
        per = get_percent(raw_att)
        msg = ""
        if att[0][0] == datetime.today():
            msg += f"""
    {rollno}:
    Today's PS attendance:
    {att[0][1]}
"""
        if datetime.today().day - att[0][0].day == 1:
            msg += f"""
    Yesterday's PS attendance:
    {att[0][1]}
"""
        msg+= f"""
    PS Attendence percentage: {per}
"""
        await message.channel.send(msg)


client.run(bot_token)