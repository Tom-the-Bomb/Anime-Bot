import discord
import json
from   discord.ext import commands

class ReactionRoles(commands.Cog):
    
    def __init__(self, bot):
		self.bot = bot
		self.rr_cache      = {}
		self.rr_channel_id = 793939009772191796
		self.load_rr_data()
	
	def load_rr_data(self) -> dict:
		with open("rr_data.json") as rr:
			with json.load(rr) as rr:
				data = rr["reaction_roles"]
				self.rr_cache = data
				return self.rr_cache
	
	async def change_role(self, reaction, is_add):
		
		if reaction.channel_id == self.rr_channel_id :
			guild     = client.get_guild(reaction.guild_id)
			member    = discord.utils.get(guild.members, id=reaction.user_id)
			emoji     = str(reaction.emoji)
			role_name = self.rr_cache.get(emoji, None)
			
			if None not in (member, role_name):
				Role = discord.utils.get(guild.roles, name=role_name)
				
				if is_add:
					await member.add_roles(Role)
				else:
					await member.remove_roles(Role)
		return

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, reaction):
		await self.change_role(reaction, True)

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, reaction):
		await self.change_role(reaction, False)
				
def setup(bot):
	bot.add_cog(ReactionRoles(bot))
	
