import fetch_web
import fetch_repository
from typing import List
from typing import Dict
from datetime import datetime
import fetch_logger

logger = fetch_logger.get_logger()

async def handle_metadata(webs:List[fetch_web.Web], repo:fetch_repository.Repository):
    for web in webs:
        metadata = repo.metadata(web.domain())
        
        if metadata:
            format_metadata(metadata, repo)
        else:
            logger.info(f"no metadata for {web.urls()}")            

def format_metadata(metadata:Dict, repo:fetch_repository.Repository):    
    if not metadata:
        return 

    meta_datetime = datetime.fromtimestamp(metadata[repo._key_last_fetch]).strftime("%a %b %d %Y %I:%M %p")
    meta_site = metadata[repo._key_site]
    meta_link = metadata[repo._key_links]
    meta_images= metadata[repo._key_images]
    print("==================")
    print("\033[31m" + "Site:" + "\033[0m" + meta_site)
    print("\033[31m" + "num_links:" + "\033[0m"+ str(meta_link) )
    print("\033[31m" + "Images:" + "\033[0m"+ str(meta_images) )
    print("\033[31m" + "Last fetched:" + "\033[0m"+meta_datetime )
    print("============")
