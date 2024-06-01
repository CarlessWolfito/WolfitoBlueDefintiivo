#to get discord.py==1.7.3, open command prompt and write "pip install discord==1.7.3" and "pip install discord.py==1.7.3"
import discord
from discord.ext import commands #importing the modules/libararys so u can use them to make ur selfbot
 
 token = os.getenv("DISCORD_BOT_TOKEN")
if not token:
    raise ValueError("El token del bot de Discord no está configurado en la variable de entorno DISCORD_BOT_TOKEN")

client = commands.Bot(command_prefix="!", self_bot=True) # creating a SELFBOT client with the help discord discord.ext with the command prefix !
 
 
@client.event # you make events like this i guess
async def on_ready(): #when the client is ready, the event is named on_ready read in their docs
    #do something when the selfbot is ready
    print("Selfbot is ready to be used.")
    print("-----------------------------")
    print("Command Prefix is !")
    #prints alot of stuff
 
 
#so our selfbot itself worked.
#lets have a little fun defining a command 
 
@client.command() # you make commands like this
async def hello(ctx): #the command name is hello, and ctx is the context.
    print("hello command was used.") #prints that the command was used.
    await ctx.send("hello command was used") #since its a async function you gotta use await to call functions i guess.
    message1 = await ctx.send("i like to do sus stuff") #message1 is the message being sent
    await message1.delete()  
# so now we are done with our event but our selfbot does nothing.
    
client.run(token, bot=False) #running the client that is NOT a bot with a token that we defined.
 
 
#okay lets retry.
