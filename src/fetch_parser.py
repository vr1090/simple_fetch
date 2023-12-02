import argparse

def getParser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("webs",nargs='*')
    parser.add_argument("-m","--metadata",action="store_true")
    return parser