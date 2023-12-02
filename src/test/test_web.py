import fetch_web
import pytest

def test_return_file_path():
    web = fetch_web.Web("https://test.com", MockWebfetcher())
    assert web.filepath() == "test.com.html"

@pytest.mark.asyncio
async def test_fetch_web():
    web = fetch_web.Web("https://test.com", MockWebfetcher() )
    assert await web.fetch() == "mock web"



class MockWebfetcher(fetch_web.WebFetcher):
    async def fetch(self,url:str)->str:
        return "mock web"