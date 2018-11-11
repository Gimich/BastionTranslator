# Work with Python 3.6
import discord
import os

client = discord.Client()

TOKEN = os.environ["TOKEN"]

gimich = os.environ["Gimich"]

bastionEmoji = str("<:Bastion:" + os.environ["Bastion"] + ">")

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	messageRecue = message.content.lower().split(" ")
	if message.author == client.user:
		return

	if "dweeee" in messageRecue and message.author.id == gimich:
		msg = (bastionEmoji + '  a dit : \"Bonjour\"'.format(message))
		await client.send_message(message.channel, msg)

	if "dwuuuuuuu" in messageRecue and message.author.id == gimich:
		msg = (bastionEmoji + ' est triste'.format(message))
		await client.send_message(message.channel, msg)

	if "dwuiii" in messageRecue and message.author.id == gimich:
		msg = (bastionEmoji + ' a dit : \"Merci\"'.format(message))
		await client.send_message(message.channel, msg)

	if "dwui" in messageRecue and message.author.id == gimich:
		msg = (bastionEmoji + ' a dit : \"Oui\"'.format(message))
		await client.send_message(message.channel, msg)

	if "dwuiiiiiii" in messageRecue and message.author.id == gimich:
		msg = (bastionEmoji + ' est content'.format(message))
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)
