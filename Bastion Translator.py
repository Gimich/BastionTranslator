# Work with Python 3.6
import discord
import os

client = discord.Client()

TOKEN = os.environ["TOKEN"]

gimich = os.environ["Gimich"]

bastionEmoji = "<:Bastion:" + os.environ["Bastion"] + ">"

@client.event
async def on_message(message):
	auteur = message.author
	
	messageRecue = message.content.lower().split(" ")
	if message.author == client.user:
		return

	if "dweeee" in messageRecue:
		msg = (auteur.username() + " : " + '  a dit : \"Bonjour\"'.format(message))
		await client.send_message(message.channel, msg)

	if "dwuuuuuuu" in messageRecue:
		msg = (auteur.username() + " : " + ' est triste'.format(message))
		await client.send_message(message.channel, msg)

	if "dwuiii" in messageRecue:
		msg = (auteur.username() + " : " + ' a dit : \"Merci\"'.format(message))
		await client.send_message(message.channel, msg)

	if "dwui" in messageRecue:
		msg = (auteur.username() + " : " + ' a dit : \"Oui\"'.format(message))
		await client.send_message(message.channel, msg)

	if "dwuiiiiiii" in messageRecue:
		msg = (auteur.username() + " : " + ' est content'.format(message))
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
