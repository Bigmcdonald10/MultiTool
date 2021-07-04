# -*- coding: utf-8 -*-
import os, sys, termcolor, discord, asyncio, random, json
from termcolor import colored 
from termcolor import cprint  
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord.ext import tasks
from discord.ext.tasks import loop
from discord.ext.commands import BucketType, cooldown, CommandOnCooldown

#Starts cog
class eco(commands.Cog):
  def __init__(self,bot):
      self.bot = bot


  

#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #--------------------------ECO SYSTEM---------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!
#    !!!!!!!COMING SOON    #---------------------------------------------------------------#    COMING SOON!!!!!!!
  
  
  




#---------------------------------------------------------------#
#---------------------------------------------------------------#
#--------------------------LEVEL SYSTEM-------------------------#
#---------------------------------------------------------------#
#---------------------------------------------------------------#




      
  @commands.Cog.listener()
  async def on_member_join(self,member):
    with open('users.json', 'r') as f:
      users = json.load(f)

    await self.update_data(users, member)

    with open('users.json', 'w') as f:
      json.dump(users, f)


  @commands.Cog.listener()
  async def on_message(self,message):
    if message.author.bot == False:
      with open('users.json', 'r') as f:
        users = json.load(f)

      await self.update_data(users, message.author)
      await self.add_experience(users, message.author, random.randint(15,25))
      await self.level_up(users, message.author, message)

      with open('users.json', 'w') as f:
        json.dump(users, f)
    await self.bot.process_commands(message)



  async def update_data(self,users, user):
    if not f'{user.id}' in users:
      users[f'{user.id}'] = {}
      users[f'{user.id}']['experience'] = 0
      users[f'{user.id}']['level'] = 1


  async def add_experience(self,users, user, exp):
    users[f'{user.id}']['experience'] += exp


  async def level_up(self,users, user, message):
      with open('levels.json', 'r') as g:
        levels = json.load(g)
      experience = users[f'{user.id}']['experience']
      lvl_start = users[f'{user.id}']['level']
      lvl_end = int(experience ** (1 / 4))
      if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end



  @commands.Cog.listener()
  async def on_member_join(self,member):
    with open('users.json', 'r') as f:
      users = json.load(f)

    await self.update_data(users, member)

    with open('users.json', 'w') as f:
      json.dump(users, f)


  @commands.Cog.listener()
  async def on_message(self,message):
    if message.author.bot == False:
      with open('users.json', 'r') as f:
        users = json.load(f)

      await self.update_data(users, message.author)
      await self.add_experience(users, message.author, random.randint(15,25))
      await self.level_up(users, message.author, message)

      with open('users.json', 'w') as f:
        json.dump(users, f)
    await self.bot.process_commands(message)
      


  async def update_data(self,users, user):
    if not f'{user.id}' in users:
      users[f'{user.id}'] = {}
      users[f'{user.id}']['experience'] = 0
      users[f'{user.id}']['level'] = 1


  async def add_experience(self,users, user, exp):
    users[f'{user.id}']['experience'] += exp



  async def level_up(self,users, user, message):
      with open('levels.json', 'r') as g:
        levels = json.load(g)
      experience = users[f'{user.id}']['experience']
      lvl_start = users[f'{user.id}']['level']
      lvl_end = int(experience ** (0.25 / 1))
      if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end


        

  @commands.command(aliases=['rank'])
  async def level(self,ctx, member: discord.Member = None):
    if not member:
      id = ctx.message.author.id
      with open('users.json', 'r') as f:
        users = json.load(f)
      lvl = users[str(id)]['level']
      embed = discord.Embed(color= discord.Color.gold())
      embed.set_author(name="Luwiz Leveling System")
      embed.add_field(name=f"{ctx.author}", value=f"Your Discord Chatting Level Is At: ****{lvl}****")
      message = await ctx.channel.send(embed=embed)
    else:
      id = member.id
      with open('users.json', 'r') as f: 
        users = json.load(f)
      lvl = users[str(id)]['level']
      embed = discord.Embed(color= discord.Color.gold())
      embed.set_author(name="Luwiz Leveling System")
      embed.add_field(name=f"{member}", value=f"is at a discord chatting level of: ****{lvl}****")
      await ctx.channel.send(embed=embed)










#tells in console if cog has been loaded
def setup(bot):
    bot.add_cog(eco(bot))
    print("""Cog: Economy
Status: Loaded""")