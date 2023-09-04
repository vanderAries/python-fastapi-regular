.DEFAULT_GOAL := run

run: src/main.py
	./.venv/bin/python src/main.py

start:
	uvicorn src.app.main:app --reload

test:
	pylint src/main.py;		\
	mypy src/main.py

install:
	python -m venv .venv
	./.venv/bin/pip install --upgrade pip
	./.venv/bin/pip install -r requirements.txt

update: requirements.txt
	./.venv/bin/pip install --upgrade pip
	./.venv/bin/pip install -r requirements.txt

clean:
	rm -rf .venv
	rm -rf .mypy_cache
	rm -rf src/__pycache__