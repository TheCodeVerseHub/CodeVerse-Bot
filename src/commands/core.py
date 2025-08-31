import discord
import os
from discord.ext import commands
from discord import app_commands
from datetime import datetime, timezone

class Core(commands.Cog):
    """Core hybrid commands: ping, info, help."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.start_time = getattr(bot, 'start_time', datetime.now(timezone.utc))

    @commands.hybrid_command(name="ping", help="Check if the bot is responsive")
    async def ping(self, ctx: commands.Context):
        """Latency check."""
        latency_ms = round(self.bot.latency * 1000)
        embed = discord.Embed(
            title="Connection Status", 
            description=f"WebSocket Latency: {latency_ms}ms",
            color=0x2ECC71
        )
        await ctx.reply(embed=embed, mention_author=False)

    @commands.hybrid_command(name="info", help="Get bot information")
    async def info(self, ctx: commands.Context):
        uptime = datetime.now(timezone.utc) - self.start_time
        embed = discord.Embed(
            title="CodeVerse Bot Information", 
            description="A professional Discord bot for programming communities",
            color=0x3498DB,
            timestamp=datetime.now(timezone.utc)
        )
        embed.add_field(name="Uptime", value=str(uptime).split('.')[0], inline=True)
        embed.add_field(name="Command Prefix", value=str(self.bot.command_prefix), inline=True)
        instance_id = os.getenv('INSTANCE_ID', 'production')
        embed.add_field(name="Instance ID", value=instance_id, inline=True)
        embed.set_footer(text=f"Instance: {instance_id}")
        await ctx.reply(embed=embed, mention_author=False)

    @commands.hybrid_command(name="bothelp", help="Show all bot commands organized by category")
    async def help_cmd(self, ctx: commands.Context):
        """Enhanced help command with organized categories."""
        embed = discord.Embed(
            title="CodeVerse Bot - Command Reference",
            description="All commands work with both prefix `?` and slash `/` notation\nExample: `?ping` or `/ping`",
            color=0x3498DB,
            timestamp=datetime.now(timezone.utc)
        )
        
        # Core Commands
        core_commands = [
            "**ping** - Check bot latency and responsiveness",
            "**info** - View bot information and uptime",
            "**diag** - Get bot diagnostics and health status",
            "**help** - Show this command reference"
        ]
        embed.add_field(
            name="Core Commands",
            value="\n".join(core_commands),
            inline=False
        )
        
        # Community Commands
        community_commands = [
            "**`quote`** - Get inspirational programming quotes",
            "**`question`** - Random programming questions for learning",
            "**`meme`** - Programming memes and humor",
            "**`suggest <text>`** - Submit suggestions to bot developers"
        ]
        embed.add_field(
            name="🎪 Community & Learning",
            value="\n".join(community_commands),
            inline=False
        )
        
        # Fun & Games Commands
        fun_commands = [
            "**`compliment [@user]`** - Send a random compliment",
            "**`dadjoke`** - Get a dad joke",
            "**`fortune`** - Programming fortune cookie",
            "**`joke`** - Programming jokes",
            "**`flip`** - Flip a coin",
            "**`8ball <question>`** - Magic 8-ball answers",
            "**`roll [NdN]`** - Roll dice (e.g., 2d6)",
            "**`rps <choice>`** - Rock Paper Scissors",
            "**`wyr`** - Would you rather questions",
            "**`hangman`** - Programming-themed hangman",
            "**`riddle`** - Interactive riddles",
            "**`trivia`** - Programming trivia questions",
            "**`kill <@user>`** - Playfully 'eliminate' a user"
        ]
        embed.add_field(
            name="🎮 Fun & Games",
            value="\n".join(fun_commands),
            inline=False
        )
        
        # Programming Utilities
        programming_commands = [
            "**`snippet <lang> <algo>`** - Code snippets (Python, JS, Java, C++)",
            "**`regex [pattern]`** - Common regex patterns (email, phone, etc.)",
            "**`bigO [complexity]`** - Big O notation explanations",
            "**`http [code]`** - HTTP status code lookup",
            "**`git [command]`** - Git command reference",
            "**`encode <format> <text>`** - Encode text (base64, url, hex, binary)",
            "**`decode <format> <text>`** - Decode text (base64, url, hex)",
            "**`hash <algo> <text>`** - Generate hashes (md5, sha1, sha256, sha512)",
            "**`json <text>`** - Format and validate JSON",
            "**`color <value>`** - Convert color formats (hex, rgb, names)",
            "**`uuid [version]`** - Generate UUIDs (v1, v4)",
            "**`timestamp [time] [format]`** - Convert timestamps"
        ]
        embed.add_field(
            name="💻 Programming Utilities",
            value="\n".join(programming_commands),
            inline=False
        )
        
        # Staff Points System
        points_commands = [
            "**`points check [@user]`** - Check points balance",
            "**`points leaderboard`** - View top staff members",
            "**`points top`** - Quick top 3 view",
            "**`points stats [@user]`** - Detailed statistics",
            "**`points history [@user]`** - Points activity log *(Mod)*",
            "**`points add <@user> <amount> [reason]`** - Award points *(Admin)*",
            "**`points remove <@user> <amount> [reason]`** - Remove points *(Admin)*",
            "**`points set <@user> <amount> [reason]`** - Set exact points *(Admin)*",
            "**`points reset <@user> [reason]`** - Reset to zero *(Admin)*",
            "**`points config <action> [value]`** - Configure system *(Admin)*"
        ]
        embed.add_field(
            name="⭐ Staff Points (Aura) System",
            value="\n".join(points_commands),
            inline=False
        )
        
        # Staff Reminder Commands (Admin only)
        reminder_commands = [
            "**`reminder-status`** - Check staff reminder status *(Admin)*",
            "**`remind-now`** - Send manual reminder to staff *(Admin)*",
            "**`staff-channel [#channel]`** - Set staff reminder channel *(Admin)*"
        ]
        embed.add_field(
            name="🔔 Staff Reminder (Admin Only)",
            value="\n".join(reminder_commands),
            inline=False
        )
        
        # Staff Shift Commands
        shift_commands = [
            "**`shift start [note]`** - Start your staff shift *(Staff)*",
            "**`shift end [note]`** - End your staff shift *(Staff)*",
            "**`shift discard`** - Discard current shift *(Staff)*",
            "**`shift admin active`** - View active shifts *(Admin)*",
            "**`shift admin history [user] [days]`** - View shift history *(Admin)*",
            "**`shift admin end <user> [reason]`** - Force end shift *(Admin)*",
            "**`shift admin stats [user] [days]`** - View shift statistics *(Admin)*",
            "**`shift admin summary [days]`** - Staff activity summary *(Admin)*",
            "**`shift settings logs [#channel]`** - Set shift log channel *(Admin)*",
            "**`shift settings addrole <role>`** - Add staff role *(Admin)*",
            "**`shift settings removerole <role>`** - Remove staff role *(Admin)*",
            "**`shift settings clearroles`** - Clear all staff roles *(Admin)*",
            "**`shift settings listroles`** - List staff roles"
        ]
        embed.add_field(
            name="⏰ Staff Shift Tracking",
            value="\n".join(shift_commands),
            inline=False
        )
        
        # Moderation Commands (Admin only)
        moderation_commands = [
            "**`purge <amount> [@user]`** - Delete messages *(Manage Messages)*",
            "**`kick <member> [reason]`** - Kick a member *(Kick Members)*",
            "**`ban <member> [days] [reason]`** - Ban a member *(Ban Members)*",
            "**`unban <user> [reason]`** - Unban a user *(Ban Members)*",
            "**`timeout <member> <minutes> [reason]`** - Timeout a member *(Moderate Members)*",
            "**`untimeout <member> [reason]`** - Remove timeout *(Moderate Members)*",
            "**`warn <member> [reason]`** - Warn a member *(Manage Messages)*",
            "**`slowmode <seconds> [#channel]`** - Set channel slowmode *(Manage Channels)*",
            "**`nick <member> [nickname]`** - Change nickname *(Manage Nicknames)*"
        ]
        embed.add_field(
            name="🛡️ Basic Moderation (Admin Only)",
            value="\n".join(moderation_commands),
            inline=False
        )
        
        # Advanced Moderation Commands
        advanced_mod_commands = [
            "**`serverinfo`** - Detailed server information",
            "**`userinfo [@user]`** - Detailed user information", 
            "**`roleinfo <role>`** - Detailed role information",
            "**`channelinfo [#channel]`** - Detailed channel information",
            "**`lockdown [#channel] [reason]`** - Lock channel *(Manage Channels)*",
            "**`unlock [#channel] [reason]`** - Unlock channel *(Manage Channels)*",
            "**`nuke [#channel] [reason]`** - Delete and recreate channel *(Manage Channels)*",
            "**`massban <user_ids> [days] [reason]`** - Mass ban users *(Ban Members)*",
            "**`listbans`** - List all banned users *(Ban Members)*",
            "**`addrole <@user> <role> [reason]`** - Add role to user *(Manage Roles)*",
            "**`removerole <@user> <role> [reason]`** - Remove role from user *(Manage Roles)*"
        ]
        embed.add_field(
            name="⚔️ Advanced Moderation (Admin Only)",
            value="\n".join(advanced_mod_commands),
            inline=False
        )
        
        # Footer with usage info
        embed.add_field(
            name="💡 Usage Tips",
            value="• Use `?command` or `/command` - both work!\n• Some commands need parameters (shown in `<>` or `[]`)\n• Admin commands require Manage Server permission\n• Staff reminders sent every 2 hours to #staff-chat (ToS compliant)\n• Staff shifts track on-duty time with database logging",
            inline=False
        )
        
        embed.set_footer(text=f"CodeVerse Bot • {len([cmd for cmd in self.bot.commands if not cmd.hidden])} commands available")
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else None)
        
        await ctx.reply(embed=embed, mention_author=False)

    @commands.hybrid_command(name="commands", help="Quick list of all available commands")
    async def commands_list(self, ctx: commands.Context):
        """Simple command list for quick reference."""
        embed = discord.Embed(
            title="⚡ Quick Command List",
            description="Use `?help` or `/help` for detailed descriptions",
            color=discord.Color.green()
        )
        
        # Get all non-hidden commands
        all_commands = []
        for cmd in sorted(self.bot.commands, key=lambda c: c.name):
            if not cmd.hidden:
                all_commands.append(f"`{cmd.name}`")
        
        # Split into chunks for better display
        chunk_size = 10
        command_chunks = [all_commands[i:i + chunk_size] for i in range(0, len(all_commands), chunk_size)]
        
        for i, chunk in enumerate(command_chunks):
            field_name = f"Commands ({i*chunk_size + 1}-{min((i+1)*chunk_size, len(all_commands))})"
            embed.add_field(
                name=field_name,
                value=" • ".join(chunk),
                inline=False
            )
        
        embed.add_field(
            name="💡 Remember",
            value="All commands work with both `?` and `/` prefixes!\nUse `?help` for full descriptions and examples.",
            inline=False
        )
        
        embed.set_footer(text=f"Total: {len(all_commands)} commands available")
        await ctx.reply(embed=embed, mention_author=False)

async def setup(bot: commands.Bot):
    await bot.add_cog(Core(bot))
