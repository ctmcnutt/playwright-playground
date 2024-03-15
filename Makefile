run-formatter:
	python3 -m black .

install-dependencies:
	pip3 install -r requirements.txt

install-browsers:
	playwright install --with-deps

run-headless:
	python3 -m pytest tests

run-headed:
	python3 -m pytest tests --headed

run-headed-slow:
	python3 -m pytest tests --headed --slowmo 1000