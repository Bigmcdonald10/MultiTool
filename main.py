

#------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#
#-----------This descriptive document for discord.py is not intended to be used for a bot,-------------------------------#
#-----------All this is for, is to help you have a more deap understanding on what each of these do!---------------------#
#-----------Using this as a default discord bot, is not only slow, but messy.. your code should be organized neatly.-----#
#------------------------------------------------------------------------------------------------------------------------#
#-----------This is just for deap learning experience, I recomend to not copy my code and use it for your self.----------#
#-----------Learn from my code and make it by your self alone.. You can always reference it!-----------------------------#
#------------------------------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#
#------------------------------- https://github.com/Bigmcdonald10/MultiTool.git -----------------------------------------#
#------------------------------------------------------------------------------------------------------------------------#









import discord,os,json
from discord.ext import commands
from discord.ext import tasks
from discord.ext.tasks import loop

def get_prefix(bot,message):          #Defining a variable that grabs the server prefix, so that it can be used at a later date. 
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    return prefixes[str(message.guild.id)] #Opening prefixes.json as a string with GuildID.

intents = discord.Intents.default()#   /// Intents ////
intents.members = True#   /// Intents ////
intents.presences = True #   /// Intents ////
language = "en"
bot = commands.Bot(command_prefix = get_prefix, intents=intents)#   /// Bot Client and commands prefix. ////
bot.remove_command('help')# /// Disabling The Default Help Command ///
os.system('clear')#   /// Clearing The Terminal ////
TOKEN = " GO HERE AND GET YOUR TOKEN  ----->>>> https://discord.com/developers/applications"
@bot.event #Bot starts and setting up first startup functions
async def on_ready():#When the bot is ready, starting up messages of the guilds that the bot is apart of...
    for guild in bot.guilds:
        print("The Servers My Bot Is In:")
        print(guild.name)


#---------------------------#
#---------------------------#
#------Custom Prefixes------#
#---------------------------#
#---------------------------#


@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)
    prefixes[str(guild.id)] = "!" #Put your default prefix here, when the bot joins a guild, the server will be assigned this prefix ( ! ).
    with open("prefixes.json","w") as f: #Grabbing above the default prefix, we are editing the Prefix for that guild and assigning it's own prefix ( ! ).
        json.dump(prefixes,f)

@bot.command()
@commands.has_permissions(administrator = True)
async def changeprefix(ctx, prefix):

    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix          #Assigning a new prefix via the command !changeprefix $ ( the new prefix would be ( $ ) ).

    with open("prefixes.json", "w") as f:
        json.dump(prefixes,f)    
    embed=discord.Embed(title=f"The prefix was changed to {prefix}", description=f"prefix changed by {ctx.author}", colour=0x30e40b)             #Making a simple Embed ( There are many ways of making an embed!!!! ).
    await ctx.send(embed=embed)

@bot.event
async def on_message(ctx):
    if 'prefix?' in ctx.content:                #Checking if [ prefix? ] is in the message content.
        with open("prefixes.json","r") as f:
            prefixes = json.load(f)
        prefix = prefixes[str(ctx.guild.id)]         #using prefix to store this data of retrieving of what the prefix is for that guild.
        embed=discord.Embed(title=f"What is my prefix?",description=f"Prefix: __**{prefix}**__",colour=0x060606)
        await ctx.channel.send(embed=embed)                 #sending the embed containing the prefix to the server.
    else:
        pass



#---------------------------#
#---------------------------#
#------Custom Statuses------#
#---------------------------#
#---------------------------#
    
@loop(seconds=60)                       #Loop through the presence changes, to have multiple!!
async def presence_change():
    await bot.change_presence(activity=discord.Game(f"help in {len(bot.guilds)} active Servers"))   #First Status Change \\\ Grabs the amount of servers in, and shows it in the status ///
    await bot.change_presence(activity=discord.Game("Put a message here for a status"))             #Second Status Change.

bot.run(TOKEN)