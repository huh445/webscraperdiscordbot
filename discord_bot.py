import discord
from discord.ext import commands
from web_scraper import WebScraper

class Discord:

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        bot = commands.Bot(command_prefix=".", intents=intents)

        self.web_scraper = WebScraper()

        @bot.event
        async def on_ready():
            print(f"Logged in as {bot.user}")

        @bot.command()
        async def page_get(ctx):
           page_list =  self.get_web()
           for page in page_list:
            await ctx.send(page)
        
        bot.run("MTI1NjE5ODk1MDM0NDQ1ODI2MQ.GA9JJo.bAdM6c-AJNkTIWaOWbEewyHKnQxi_LzYnsPuOg")
    
    def get_web(self):
        page = self.web_scraper.web_scraper()
        page_list = [page[i:i+1500] for i in range(0, len(page), 1500)]
        return page_list