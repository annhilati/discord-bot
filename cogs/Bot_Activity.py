import datetime
import discord
from discord.ext import commands, tasks
from itertools import cycle

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
    await client.add_cog(Bot_Activity(client))

class Bot_Activity(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.bot_statuses = cycle(["mit der Discord-API", "mit Python-Bots"])  # Liste aller Bot-Status
        self.change_status.start()  # Startet den Bot-Status-Loop, wenn der Cog geladen wird

    @tasks.loop(seconds=5)
    async def change_status(self):
        # Ändert den Bot-Status
        await self.client.change_presence(activity=discord.Game(next(self.bot_statuses)))

    @change_status.before_loop
    async def before_change_status(self):
        # Warte darauf, dass der Bot bereit ist, bevor der Loop startet
        await self.client.wait_until_ready()

    @commands.Cog.listener()
    async def on_ready(self):
        log(f"[COGS] {__name__} is ready")