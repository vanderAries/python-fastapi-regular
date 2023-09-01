.DEFAULT_GOAL := run

run: src/main.py
	./.venv/bin/python src/main.py

install:
	python -m venv .venv
	./.venv/bin/pip install --upgrade pip
	./.venv/bin/pip install -r requirements.txt

update: requirements.txt
	./.venv/bin/pip install --upgrade pip
	./.venv/bin/pip install -r requirements.txt

clean:
	rm -rf .venv
	rm -rf __pycache__