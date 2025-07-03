# Imports
import discord
import outputHandling
import threading
import os
from discord.ext import commands
from Data.token import Token


# Main Discord Class
class DiscordHandler:
    def __init__(self):
        self.token = Token
        self.client = commands.Bot(command_prefix='/', intents=discord.Intents.all())
        self.__register_events()
        self.__register_commands()


    @staticmethod
    def __shutDown():
        os.system("shutdown /s /t 1")

    def __register_events(self):
        @self.client.event
        async def on_ready():
            await self.client.get_user(500681595619901451).send("Jarvis 3 is ready to go! :D!!")


    def __register_commands(self):
        @self.client.command()
        async def initiate_shutdown(ctx):
            outputHandling.Speaker().speak("Initiating Remote Termination Sequence! Goodbye!")
            await ctx.send("Initiating Remote Termination Sequence!")
            self.__shutDown()


    def run(self):
        disthread = threading.Thread(target=self.client.run, args=[self.token])
        # disthread.daemon = True
        disthread.start()


# Start the bot
if __name__ == "__main__":
    bot_handler = DiscordHandler()
    bot_handler.run()
    while True:
        pass
    print('asd')