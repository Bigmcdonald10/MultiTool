# -*- coding: utf-8 -*-
import discord, asyncio
from termcolor import colored 
from termcolor import cprint 
from discord.ext import commands
from random import *
class listens(commands.Cog):
  def __init__(self,bot):
      self.bot = bot




  @commands.Cog.listener()
  async def on_error(self,error,ctx):
    if isinstance(error, discord.errors.Forbidden):
      await ctx.channel.send("I don't have permissions please give me permissions")
      



 
  @commands.Cog.listener()
  async def on_member_join(self,member):
    channel = member.guild.system_channel
    if channel is not None: 
      embed = discord.Embed(colour=0x06e4ee)
      embed.set_author(name=f"{member.name}")
      embed.add_field(name="Welcome!", value=f"Please welcome {member.mention} to the server!")
      embed.set_image(url=member.avatar_url)  
      await channel.send(embed=embed)
    else:
      pass



  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if isinstance(error, commands.errors.CommandOnCooldown):
     embed = discord.Embed(
       title = 'Cooldown Timer',
       description = f'try again in {error.retry_after:,.2f} seconds',
       color = discord.Color.blue())
     embed.set_author(name='BOT')
     await ctx.send(embed=embed)
    else:
      raise error







  @commands.Cog.listener()
  async def on_guild_join(self,guild):
    channel = guild.system_channel
    if channel is None:
      pass
    else:
      embed = discord.Embed(title = f"👋 Hello! Thanks for adding me to the server", colour = 0x1df30e) 
      embed.add_field(name=f"defult prefix is ! \nto get help say help ", value=f"for any other questions join our [support server](https://discord.gg/dnBcSafW9Z)\nmake sure i have admin permissions so you can get the most out of me")
      await channel.send(embed=embed)






#tells in console if cog has been loaded
def setup(bot):
    bot.add_cog(listens(bot))
    print("""Cog: listens
Status: Loaded""")