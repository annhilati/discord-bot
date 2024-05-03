import datetime
import discord
from discord.ext import commands
import os

#-------------------------------------------------#
#             Funktionsdefinitionen               #
#                     log()                       #
#-------------------------------------------------#

def log(text):
    return print("[" + datetime.datetime.now().strftime("%H:%M:%S") + "] " + text)

#-------------------------------------------------#
#                cog-Deklaration                  #
#-------------------------------------------------#

async def setup(client):
    await client.add_cog(Commands_Snippet(client))

class Commands_Snippet(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] Commands_Snippet is ready")

    #-------------------------------------------------#
    #              Snippet-Supercommand               #
    #-------------------------------------------------#

    @commands.command()
    async def snippet(self, ctx, arg1=None, arg2=None):
        if arg1 == "discord.py" or arg1 == "d.py":
            if arg2 == "cog":
                with open("assets/snippets/cog.py", 'r') as file:
                    content = file.read()
                await ctx.reply(f"## discord.py Cog\n```py\n{content}\n```", mention_author=False)

        #-------------------------------------------------#
        #                  Error Raising                  #
        #-------------------------------------------------#

            elif arg2 == None:
                raise commands.MissingRequiredArgument(param=commands.Parameter(name='arg2', annotation=str, kind=3))
            else:
                raise commands.BadArgument("Unbekanntes Snippet")
        elif arg1 == None:
            raise commands.MissingRequiredArgument(param=commands.Parameter(name='arg1', annotation=str, kind=3))
        else:
            raise commands.BadArgument("Unbekanntes Snippet")