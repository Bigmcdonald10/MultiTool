# -*- coding: utf-8 -*-
import discord
import asyncio
from termcolor import colored 
from termcolor import cprint 
from discord.ext import commands
from discord.ext.commands import BucketType


#Starts cog
class moderation(commands.Cog):
  def __init__(self,bot):
      self.bot = bot
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def unmute(self, ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title=f"{member} was unmuted by {ctx.author}", colour=0x0ef3f0)
    embed.set_author(name="unmute command 🔈 ", icon_url=member.avatar_url)
    await ctx.send(embed=embed)
  





  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def mute(self, ctx, member: discord.Member, *, reason = "unspecified"):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name = "Muted")
    
    if not mutedRole:
      mutedRole = await guild.create_role(name = "Muted", colour=0x070606)

      for channel in guild.channels:
        await channel.set_permissions(mutedRole, speak = False, send_messages = False, read_message_history = False, read_messages = True)
    await member.add_roles(mutedRole, reason = reason) 
    embed = discord.Embed(title=f"{member} was muted by {ctx.author}", colour=0xf10a0a)
    embed.set_author(name="mute command", icon_url=member.avatar_url)
    embed.add_field(name=f"reason - {reason}", value="🔇")
    await ctx.send(embed=embed)



  @commands.Cog.listener()
  async def on_member_join(self, member):
    if member.guild.id == 839307082503159859:
      join_role = discord.utils.get(member.guild.roles, name='Member')
      await member.add_roles(join_role)
      





  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member: discord.Member=None):
    embed = discord.Embed(color= discord.Color.red(), timestamp=ctx.message.created_at)
    embed.add_field(name="Luwiz BanHammer", value="****{}**** was banned" .format(member.name), inline=False)
    await ctx.send(embed=embed)
    await member.ban()


  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member: discord.Member=None,*, reason = "unspecified"):
    embed=discord.Embed(color= discord.Color.red(), timestamp=ctx.message.created_at)
    embed.add_field(name=f"{member} was kicked by {ctx.author}", value=f"reason: - {reason}")
    await ctx.send(embed=embed)
    await member.kick()



  @commands.command()
  @commands.has_permissions(administrator=True)
  @commands.cooldown(1, 5, BucketType.guild)
  async def embed(self, ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(color= discord.Color.light_gray())
    embed.set_author(name="Luwiz Embeder")
    embed.add_field(name=f"{ctx.author} embeded", value=f"{message}")
    message = await ctx.channel.send(embed=embed)
    await ctx.message.delete()



  @commands.command()
  @commands.has_permissions(kick_members=True)
  @commands.cooldown(1, 2, BucketType.guild)
  async def warn(self, ctx, member, *, reason = "unspecified"):
    await ctx.message.delete()
    embed = discord.Embed(colour=0xeba309)
    embed.add_field(name="Luwiz mod warner", value=f"{ctx.author.mention} warned {member}\n reason - {reason}")
    await ctx.channel.send(embed=embed)






  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def purge(self, ctx, limit : int):
    await ctx.channel.purge(limit=limit+1)
    message = await ctx.send(f'I have purged {limit} messages')
    await asyncio.sleep(10)
    await message.delete()




  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def cdelay(self,ctx,seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"{ctx.author} has changed the slowmode to {seconds}!")

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def cname(self,ctx,*,name):
    await ctx.channel.edit(name=name)
    await ctx.channel.send(f"{ctx.author.mention} has chganged the name to {name}")
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def topic(self,ctx,*,description):
    await ctx.channel.edit(topic=description)
    await ctx.channel.send(f"{ctx.author.mention} has set the channel topic to {description}")

  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def vcmute(self, ctx, member: discord.Member):
    await member.edit(mute=True)


  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def vcunmute(self, ctx, member: discord.Member):
    await member.edit(mute=False)


#tells in console if cog has been loaded
def setup(bot):
    bot.add_cog(moderation(bot))
    print("""Cog: Moderation
Status: Loaded""")