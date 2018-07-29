import subprocess
import requests
import time

port = '8080'
server_process = None 

def start_server():
    server = ["python3.6", "../pokerserv.py", "--port", port ]
    print('starting server')
    print(server)
    global server_process
    server_process = subprocess.Popen(server)
    time.sleep(3)


def stop_server():
    server_process.terminate()
    print('server stopped')

def setup_module():
    start_server()


def teardown_module():
    stop_server()


def test_best_hands():
    hand_n_deck_input = { 'hand_n_deck_data'  : [
        { 'hand' : 'TH JH QC QD QS', 'deck' :   'QH KH AH 2S 6S', 'ranking' : 'straight-flush' } , 
        { 'hand' : '2H 2S 3H 3S 3C', 'deck' :   '2D 3D 6C 9C TH', 'ranking' : 'four-of-a-kind' },
        { 'hand' : '2H 2S 3H 3S 3C', 'deck' :   '2D 9C 3D 6C TH', 'ranking' : 'full-house' },
        { 'hand' : '2H AD 5H AC 7H', 'deck' :   'AH 6H 9H 4H 3C', 'ranking' : 'flush' },
#        { 'hand' : 'AC 2D 9C 3S KD', 'deck' :   '5S 4D KS AS 4C', 'ranking' : 'straight' } ,  
        { 'hand' : 'KS AH 2H 3C 4H', 'deck' :   'KC 2C TC 2D AS', 'ranking' : 'three-of-a-kind'},
        { 'hand' : 'AH 2C 9S AD 3C', 'deck' :   'QH KS JS JD KD', 'ranking' : 'two-pairs'},
        { 'hand' : '6C 9C 8C 2D 7C', 'deck' :   '2H TC 4C 9S AH', 'ranking' : 'one-pair' },
        { 'hand' : '3D 5S 2H QD TD', 'deck' :   '6S KH 9H AD QH', 'ranking' : 'highest-card'}
    ] }

    r = requests.post('http://localhost:{port}/besthand'.format(port=port), hand_n_deck_input ) 
    assert r.status_code == 200
    assert json.loads(r.text)

