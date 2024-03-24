PROJECT_FILE = pyproject.toml
REQ_NAME = requirements.txt
REQ_DEV_NAME = requirements-dev.txt

uv-compile:
	uv pip compile --extra dev -o $(REQ_DEV_NAME) $(PROJECT_FILE)
	uv pip compile --constraint=$(REQ_DEV_NAME) --output-file=$(REQ_NAME) $(PROJECT_FILE)

uv-install: uv-compile
	uv pip install -r requirements.txt

uv-install-dev: uv-compile
	uv pip install -r requirements-dev.txt
