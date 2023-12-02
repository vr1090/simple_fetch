from urllib.parse import urlparse
import fetch_logger
import requests
from typing import List
from typing import Callable
import aiohttp

logger = fetch_logger.get_logger()

class WebFetcher:
    async def fetch(self,url:str)->str:
        return ""

class Web:
    def __init__(self,web:str, web_fetch:WebFetcher):
        self._web = web
        self._web_fetcher = web_fetch
        self._internal_parse()

    def _internal_parse(self):
        self._parse = urlparse(self._web)
    
    def filepath(self)-> str:
        return f"{self._parse.netloc}.html"

    def domain(self)->str:
        return self._parse.netloc
    
    def urls(self)->str:
        return self._web
    
    async def fetch(self)-> str:
        try:
            return await self._web_fetcher.fetch(self._web)
        except Exception as e:
            logger.error(f"failed fetch {self._web}, return empty string")
            raise e

class RequestWebFetcher(WebFetcher):
    async def fetch(self,url:str)->str:
        try:
            response = requests.get(url)
            return response.text
        except Exception as e:
            raise e

class AioWebFetcher(WebFetcher):
    async def fetch(self,url:str)->str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                return text


def generateWeb(urls:List[str],web_generator:Callable[[str],Web])-> List[Web]:
    webs = []

    for url in urls:
        try:
            web = web_generator(url)

            if web.filepath() !=".html":
                webs.append(web)
    
        except Exception as e:
            logger.info(f"error can not handle {url} {e}")
    
    return webs
            



        


