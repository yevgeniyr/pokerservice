init:
	pip install -r requirements.txt


test:
	cd tests; PYTHONPATH=.. python3.6 -m pytest


start_server:
	python3.6 pokerserv.py &
    
.PHONY: init test start_server
