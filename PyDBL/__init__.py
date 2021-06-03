import requests
import aiohttp


class InvalidApiKey(Exception):

    def __init__(self, message="The api key is invalid."):
        self.message = message
        super().__init__(self.message)

class DiscordBotsList:

    def __init__(self,apikey:str):
        super().__init__()
        self.url = "https://api.discordbotslist.co/"
        self.apikey = apikey
    
    
    async def getStats(self, id: int):
        """Get statistics for your bot in json format"""
        h = {"authorization" : self.apikey}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.discordbotslist.co/v1/public/bot/{id}", headers=h) as res:
                text = await res.text()
                return text

    async def getReviews(self, id: int):
        """Get reviews for your bot in json format"""
        h = {"authorization" : self.apikey}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.discordbotslist.co/v1/public/bot/{id}/reviews", headers=h) as res:
                text = await res.text()
                return text

    async def postServerCount(self, id: int , bot):
        """Get reviews for your bot in json format"""
        h = {"authorization": self.apikey , "content-type" : "application/json"}
        b = "{serverCount: int(len(bot.guilds))}"
        """async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.discordbotslist.co/v1/public/bot/{id}/stats", headers=h , body=b) as res:
                text = await res.text()
                return text"""
        re = requests.post(f"https://api.discordbotslist.co/v1/public/bot/{id}/stats", headers=h, data=b)
        print(re.text)
    


        

