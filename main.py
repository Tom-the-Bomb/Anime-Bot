import discord
from discord.ext import commands
from datetime import datetime as dt
from help import HelpCommand
import os

class AnimeBot(commands.Bot):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BotToken = os.getenv("TOKEN")
        self.invite_url = "https://discord.gg/SgZdhZcKua"
        self.vote_url      = "https://top.gg/servers/804284010900750367"
        self.welcome_channel = self.get_channel(804284011371167795)
        
    async def on_connect(self):
        print("Bot is connected.")
        
    async def on_ready(self):
        print("Bot is ready")
        
    async def on_member_join(self, member):
        embed = discord.Embed(
            title = "",
            description = "",
            color = discord.Color.red(),
            timestamp = dt.utcnow(),
            url = self.server_invite,
        )
        embed.set_thumbnail(url=member.avatar_url)
        return await self.welcome_channel.send(embed=embed)
    
    async def on_member_remove(self, member):
        return await self.welcome_channel.send(
            f"Oof, {member.name} left us :("
        )

    async def load_all_cogs(self):
        await self.wait_until_ready()
        try:
            for filename in os.listdir("./cogs"):
                if filename.endswith(".py"):
                    self.load_extension(f"cogs.{filename[:-3]}")
                    print(f"🔁 cogs.{filename[:-3]} is loaded and ready")
        except:
            pass
        
        
 Anime = AnimeBot(
     command_prefix = "?",
     intents = discord.Intents.all(),
     case_insensitive = True, 
     help_command = HelpCommand(),
     description = "A simple bot for an anime server"
 )

if __name__ == "__main__":
    Anime.run(Anime.BotToken)
