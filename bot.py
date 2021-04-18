import discord
from discord.ext import commands
from discord_slash import SlashCommand
import config

bot = commands.Bot(command_prefix="!")
slash = SlashCommand(bot, sync_commands=True)
guild_ids = [config.env['guildId']]

@bot.event
async def on_ready():
    print('Bot online.')

@slash.slash(
    name="test",
    description="Test the discord bot",
    guild_ids=guild_ids
)
async def _test(ctx):
    embed = discord.Embed(
        title="Embed Title",
        description= "Embed Description\n**New Line in Bold**",
        colour=0x4fb1ed
    )

    await ctx.send(embed=embed)

bot.run(config.env['token'])
