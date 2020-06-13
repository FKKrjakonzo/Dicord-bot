import discord, asyncio
from discord.ext import commands
from obed import get_obed
from functions import *
import time
from mail_checker import Mailer



bot = commands.Bot(command_prefix='$')
token = 'XXXXX'

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	await bot.change_presence(activity=discord.Game(name="Test"))

@bot.command()
async def obed(ctx):
	data = get_obed()
	reactions = get_options(data)
	await send("Obed", converttostr(data, reactions), reactions, 0000000000)

async def wait_for():
	await bot.wait_until_ready()
	mailer = Mailer()
	while bot.is_ready():
		screensaver()
		for i in mailer.search_for_unseen():
			await send("Mail", i, [], 0000000000)
		await asyncio.sleep(30)

async def send(title, message, reactions, channel):
	embed = discord.Embed(title=title, description=''.join(message), colour=0xee7400)
	react_message = await bot.get_channel(channel).send(embed=embed)
	for reaction in reactions:
		await react_message.add_reaction(reaction)

bot.loop.create_task(wait_for())
bot.run(token)

