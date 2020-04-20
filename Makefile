.PHONY: run test watch install clean
# A simple wrapper for running shared commands

run:
	python3 parent.py

test:
	python3 test.py

watch:
    #pywatch "python3 parent.py" ./src/*.py