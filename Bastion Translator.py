# Work with Python 3.6
import discord
import os
import time
import re

client = discord.Client()

TOKEN = os.environ["TOKEN"]

gimich = os.environ["Gimich"]

bastionEmoji = "<:Bastion:" + os.environ["Bastion"] + ">"

@client.event
async def on_message(message):
	if isinstance(message.author.nick, str):
		auteur = message.author.nick
	else:
		auteur = message.author.name
		
	messageRecue = re.sub('[.,!?;:/]', ' ', message.content)
	messageRecue = messageRecue.lower().split(' ')
			   
	if message.author == client.user:
		return

	if "dweeee" in messageRecue:
		if (message.timestamp.time().hour + 1) % 24 < 18 and (message.timestamp.time().hour + 1) %24 > 4:
			msg = (auteur + ' dit : \"Bonjour\"'.format(message))
		else : msg = (auteur + ' dit : \"Bonsoir\"'.format(message))
		await client.send_message(message.channel, msg)

	for i in range(len(messageRecue)):
		dwuiii = messageRecue[i].split('i')
		dwuuu = messageRecue[i].split('u')
		if len(dwuiii)>7 and dwuiii[0] == "dwu":
			msg = (auteur + ' est content'.format(message))
			await client.send_message(message.channel, msg)
		if len(dwuuu)>7 and dwuuu[0] == "dw":
			msg = (auteur + ' est triste'.format(message))
			await client.send_message(message.channel, msg)
	
	if "dwuiii" in messageRecue:
		msg = (auteur + ' dit : \"Merci\"'.format(message))
		await client.send_message(message.channel, msg)

	if "dwui" in messageRecue:
		msg = (auteur + ' dit : \"Oui\"'.format(message))
		await client.send_message(message.channel, msg)
		
	if "dwueee" in messageRecue:
		msg = (auteur + ' dit : \"Bien\"'.format(message))
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
