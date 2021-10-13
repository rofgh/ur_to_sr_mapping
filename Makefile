.PHONY: run test watch install clean
# A simple wrapper for running shared commands

install:
	echo "Install flake8 linter, install pywatch yourself."
	pip install flake8

full:
	python3 parent.py True True False all_all

run:
	python3 parent.py False False False run

test:
	python3 test.py

watch:
	echo "Watching for changes to .py files in /src/"
	pywatch "python parent.py" ./src/*.py

lint:
	echo "Linting code for Python syntax errors or undefined names"
	flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics