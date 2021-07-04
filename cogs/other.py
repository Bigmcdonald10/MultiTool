# -*- coding: utf-8 -*-
import discord,json, requests
from termcolor import colored 
from termcolor import cprint 
from discord.ext import commands
from mojang import MojangAPI



class other(commands.Cog):
  def __init__(self,bot):
      self.bot = bot

  @commands.command()
  async def pfp(self, ctx, member: discord.Member=None):
    if member is None: 
      with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
      embed = discord.Embed(color=discord.Colour.blue())
      embed.add_field(name=f"Showing Avatar For ****{ctx.author.name}****", value="Avatar")
      embed.set_image(url=ctx.author.avatar_url)
      embed.set_footer(text=f"If you would like to show someone elses pfp, Do {prefixes[str(ctx.guild.id)]}pfp @example")
      await ctx.send(embed=embed)
    else:
      embed = discord.Embed(color=discord.Colour.green())
      embed.add_field(name=f"Showing Avatar For ****{member.name}****", value="Avatar")
      embed.set_image(url=member.avatar_url)
      await ctx.send(embed=embed)

  @commands.command()
  async def ping(self, ctx):
    embed=discord.Embed(title=f"bot latency", description=f"{round(self.bot.latency * 1000)}ms", colour=0x0e0ff3)
    #await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")
    await ctx.send(embed=embed)




  


#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #-------------------------HYPIXEL API---------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!





#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #-------------------------HYPIXEL API---------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!




def setup(bot):
    bot.add_cog(other(bot))
    print("""Cog: other
Status: Loaded""")