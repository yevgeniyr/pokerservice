init:
	pip install -r requirements.txt


test:
	python3.6 -m pytest tests/


start_server:
	python3.6 pokerserv.py &
    
.PHONY: init test start_server
