init:
	pip install -r requirements.txt

test:
	python3.6 tests


.PHONY: init test
