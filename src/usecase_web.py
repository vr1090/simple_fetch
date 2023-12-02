import asyncio
import fetch_web
from typing import List
import fetch_logger
import fetch_repository

logger=fetch_logger.get_logger()

async def handle_webs(webs:List[fetch_web.Web], repo:fetch_repository.Repository):
    tasks = []
    
    for web in webs:
        task = asyncio.Task( downloadWeb(web, repo) )
        tasks.append(task)

    await asyncio.gather(*tasks)
    

async def downloadWeb(web:fetch_web.Web, repo:fetch_repository.Repository):
    try:
        file = web.filepath()
        logger.debug(f"start fetch {file}")
        content = await web.fetch()
        repo.save(file, content)
        repo.analyze(web.domain(), content)
        logger.debug(f"end fetch {file}")
    except Exception as e:
        logger.error(f"failed to fetch {web.urls()} {e}")
        return False

    return True
