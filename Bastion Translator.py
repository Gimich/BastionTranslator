# Work with Python 3.6
import discord
import os

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
		
	messageRecue = message.content.lower().split(" ")
	
	if message.author == client.user:
		return

	if "dweeee" in messageRecue:
		msg = (auteur + ' a dit : \"Bonjour\"'.format(message))
		await client.send_message(message.channel, msg)

	for i in range(len(messageRecue)):
		dwuiii = messageRecue[i].split('i')
		dwuuu = messageRecue[i].split('u')
		if len(dwuiii)>7:
			msg = (auteur + ' est content'.format(message))
			await client.send_message(message.channel, msg)
		if len(dwuuu)>7:
			msg = (auteur + ' est triste'.format(message))
			await client.send_message(message.channel, msg)
	
	if "dwuiii" in messageRecue:
		msg = (auteur + ' a dit : \"Merci\"'.format(message))
		await client.send_message(message.channel, msg)

	if "dwui" in messageRecue:
		msg = (auteur + ' a dit : \"Oui\"'.format(message))
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
