init:
	pip install -r requirements.txt


test:
	cd tests; PYTHONPATH=.. python3.6 -m pytest


start:
	python3.6 pokerserv.py &

stop:
	PYTHONPATH=. python3.6 ./bin/stop_server.py 
    
    
.PHONY: init test start
