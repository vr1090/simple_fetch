import fetch_logger
import fetch_parser
import fetch_repository
import fetch_web
import asyncio
import usecase_web
import usecase_metadata

logger = fetch_logger.get_logger()
repo = fetch_repository.SoupRepository()
webFetcher = fetch_web.AioWebFetcher()

def web_generator(url:str):
    try:
        web = fetch_web.Web(url,webFetcher)
        return web
    except Exception as e:
        logger.error(f"failed to parse {url} {e}")

async def main():
    parser = fetch_parser.getParser()
    args = parser.parse_args()
    webs = fetch_web.generateWeb(args.webs,web_generator)


    if not args.webs:
        parser.print_help()
    if args.metadata:
        await usecase_metadata.handle_metadata(webs,repo)
    else:
        await usecase_web.handle_webs(webs, repo)


asyncio.run(main())


