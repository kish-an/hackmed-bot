import discord
from discord.ext import commands
from discord_slash import SlashCommand
import config
from countdown import print_time

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)
guild_ids = [config.env['guildId']]

@bot.event
async def on_ready():
    print('Bot online.')

@slash.slash(
    name="time",
    description="Find out how much time you have left for hacking\u2004⏰",
    guild_ids=guild_ids
)
async def time(ctx):
    embed = discord.Embed(
        title="Time remaining \u2004⏰",
        description= f"{print_time()}\n\n[**Live Countdown**](https://kish-an.github.io/hackmed-countdown/)",
        colour=0x4fb1ed
    )

    await ctx.send(embed=embed)

bot.run(config.env['token'])
