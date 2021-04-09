import discord
from   discord.ext import commands, menus

class HelpPaginator(menus.ListPageSource):

    def __init__(self, ctx, bot, entries, *, per_page=1):
        self.ctx = ctx
        self.bot = bot
        super().__init__(entries, per_page=per_page)

    async def format_page(self, menu: menus.Menu, page):
        sep = "\n- "
        embed = discord.Embed(
            title = "Commands Help!",
            description = f"Type `.help [command]` to get more info on a certain command\n━━━━━━━━━━━━━━━━━━━━━━━━━\n\n```diff\n- {sep.join(page)}\n```",
            color = discord.Color.purple(),
            timestamp = dt.utcnow(),
        )
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(
            text=f"Requested by {self.ctx.author.name} •  page {menu.current_page+1}/{self.get_max_pages()}", 
            icon_url=self.ctx.author.avatar_url,
        )
        return embed

class HelpCommand(commands.HelpCommand):
    
    async def send_bot_help(self, mapping):
        pages = [[c.qualified_name for c in self.context.bot.cogs[cog].walk_commands()] for cog in self.context.bot.cogs]
        
        pages = HelpPaginator(self.context, bot=self.context.bot, entries=pages)
        paginator = menus.MenuPages(source=pages, timeout=None, delete_message_after=True)
        return await paginator.start(self.context)
        
    async def send_command_help(self, command):
        
        embed = discord.Embed(
            title = "." + command.qualified_name,
            description = (
                "**Usage**\n"
                f"```powershell\n.{command.qualified_name} {command.signature}\n```\n"
                "**Aliases**"
                f"`{", ".join(command.aliases) if command.aliases else "no aliases"}`\n"
            ),
            color = discord.Color.gold()
        )
        embed.add_field(
            name = "━━━━━ Description ━━━━━", 
            value = command.description or "-"
        )
        
        if isinstance(command, commands.Group):
            embed.add_field(name="Subcommands", value=" • " + "\n • ".join([c.qualified_name for c in command.commands]), inline=False)
            
        embed.set_footer(
            text="[ ]  is optional and < > is required", 
            icon_url=self.context.bot.user.avatar_url
        )
        return await self.context.send(embed=embed)
   
