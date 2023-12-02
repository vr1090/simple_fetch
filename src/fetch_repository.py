import fetch_logger
import datetime
from pathlib import Path
import threading
import json
from bs4 import BeautifulSoup

logger = fetch_logger.get_logger()


class Repository:
    _db_name="repo.json"
    _key_site="site"
    _key_links="links"
    _key_images="images"
    _key_last_fetch="last_fetch"
    
    def save(self,filename:str, content:str)-> bool:
        return False

class SoupRepository(Repository):


    def __init__(self):
        self.file_lock = threading.Lock()
        self.repo_lock = threading.Lock()
        
        self.repo = {}

        db_path = Path(self._db_name)

        if db_path.exists():
            self._load_repo()
        
        
    def _load_repo(self):
        with self.file_lock:
            with self.repo_lock:
                with open(self._db_name,"r") as fp:
                    try:
                        self.repo = json.load(fp)
                    except Exception as e:
                        self.repo = {}
                        

    def _save_repo(self):
       with self.file_lock:
           with self.repo_lock:
               with open(self._db_name,"w") as fp:
                   json.dump(self.repo, fp) 

    def save(self,filename:str,content:str)-> bool:
        if not content:
            return False

        try:
            with open(filename,"w") as file:
                file.write(content)
                file.close()
        except Exception as e:
            logger.error(f"error save {filename} {e}")
            return False

        return True

    def analyze(self,site:str, content:str)-> bool:
        try:
            now_timestamp = datetime.datetime.now().timestamp()
            analyze= {}
            analyze[self._key_last_fetch] = now_timestamp
            analyze[self._key_site] = site
            soup=BeautifulSoup(content,'lxml')

            all_links = soup.find_all("a")
            all_img = soup.find_all("img")
            analyze[self._key_images] = len(all_img)
            analyze[self._key_links] =len(all_links)

            with self.repo_lock:
                self.repo[site] = analyze
            
            self._save_repo()

        except Exception as e:
            raise e

        return True

    def metadata(self,site:str)->dict:
        return self.repo.get(site,{})


