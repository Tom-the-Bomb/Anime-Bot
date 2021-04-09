import discord
from   discord.ext import commands

class Info(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="vote", description="vote for us on top.gg")
    async def vote(self, ctx):
        return await ctx.send(
            "**Vote for us**\n"
            self.bot.vote_url
        )

    @commands.command(name="invite", description="Invite link to the server")
    async def invite(self, ctx):
        return await ctx.send(
            self.bot.invite_url
        )
      
def setup(bot):
    bot.add_cog(Info(bot))
          
