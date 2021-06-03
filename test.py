import PyDBL
import discord
from discord.ext import commands
api = PyDBL.DiscordBotsList("key")



bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Ready!")
    await api.postServerCount(id, bot)
    print("Posted server cont")
    print(len(bot.guilds))

@bot.command()
async def stats(ctx):
    await ctx.send(await api.getStats(id))


@bot.command()
async def review(ctx):
    await ctx.send(await api.getReviews(id))



bot.run("token")
