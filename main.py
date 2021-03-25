import discord
from discord.ext import commands
import os

class AnimeBot(commands.Bot):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.BotToken = os.getenv("TOKEN")
        
    async def on_connect(self):
        print("Bot is connected.")
        
    async def on_ready(self):
        print("Bot is ready")

    
        
