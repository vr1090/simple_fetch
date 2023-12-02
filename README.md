## Simple fetch
### how to use
```
usage: fetch [-h] [-m] [webs ...]

positional arguments:
  webs

options:
  -h, --help      show this help message and exit
  -m, --metadata
```

fetch website:
```
./fetch https://google.com https://playstation.com
```

fetch metadata:
```
./fetch --metadata https://www.google.com
```

### tech stack
- python 3.12
- asyncio
- docker
- pyinstaller

### requirement to build
- python3.12
- pip3
- pyinstaller
- docker
- make

### how to build
- execute ```make build```
- a dist folder, consist of of executable program ```fetch```

### docker version
- execute ```docker build -t fetch:latest .```
- run: ```docker run -it fetch:latest```