.PHONY: build
.PHONY: clean

clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./fetch
	rm -rf ./__pycache__
	rm -rf ./.pytest_cache
	rm -rf ../src/__pycache__
	rm -rf ./src/.pytest_cache
	rm -rf ./*/__pycache__
	rm -rf ./*.html
	rm -rf ./*.json

build: clean
	pip install -r requirements.txt
	pytest --rootdir=src
	pyinstaller main.spec