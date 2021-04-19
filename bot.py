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

@slash.slash(
    name="schedule",
    description="Events schedule for HackMed 2021 \u2004🗓️",
    guild_ids=guild_ids
)
async def schedule(ctx):
    await ctx.send(
"""
**Events Schedule** \u2004🗓️
```c
+========================================+===================================+
|                Saturday                |              Sunday               |
+========================================+===================================+
| 08:00 - Registration begins            | 09:00 - Morning activity          |
+----------------------------------------+-----------------------------------+
| 09:30 - Opening ceremony               | 11:30 - Pitching Workshop         |
+----------------------------------------+-----------------------------------+
| 10:00 - Hacking starts & Team building | 14:00 - Hacking stops             |
+----------------------------------------+-----------------------------------+
| 11:30 - Innovation skills              | 15:00 - Demos time                |
+----------------------------------------+-----------------------------------+
| 13:00 - Cyberselves Workshop           | 16:45 - Finalists' presentations  |
+----------------------------------------+-----------------------------------+
| 16:00 - Start-ups come from Hackathons | 17:45 - Awards & closing ceremony |
+----------------------------------------+-----------------------------------+
| 19:00 - Evening activity: Pictionary!  | 18:30 - The end!                  |
+----------------------------------------+-----------------------------------+
```
"""
    )

@slash.slash(
    name="music",
    description="Listen along to the HackMed 2021 spotify playlist\u2004🥳",
    guild_ids=guild_ids
)
async def music(ctx):
    msg = "**Spotify Playlist** 🎵 \nhttps://open.spotify.com/playlist/0JN8JvqQXKvO9zBfPx7bnO?si=f80ab81164354955>"

    await ctx.send(msg)

bot.run(config.env['token'])
