import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command(name='mute', help='Mutes a specified user')
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, time: int, *, reason=None):
    mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(mute_role)
    await ctx.send(f'{member} has been muted for {time} minutes. Reason: {reason}')

@bot.command(name='unmute', help='Unmutes a specified user')
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(mute_role)
    await ctx.send(f'{member} has been unmuted.')

@bot.command(name='ban', help='Bans a specified user')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} has been banned. Reason: {reason}')

bot.run('YOUR_BOT_TOKEN_HERE')
