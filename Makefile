.PHONY: start clean test

start:
	export FLASK_APP=app.py; python -m flask run

clean:
	rm -rf *.pyc

test:
	python -m unittest test
