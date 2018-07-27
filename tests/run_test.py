import subprocess
import requests

port = 8080
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
    hand_n_deck_input = {
        'TH JH QC QD QS QH KH AH 2S 6S' : 'straight-flush', 
        '2H 2S 3H 3S 3C 2D 3D 6C 9C TH' : 'four-of-a-kind', 
        '2H 2S 3H 3S 3C 2D 9C 3D 6C TH' : 'full-house',
        '2H AD 5H AC 7H AH 6H 9H 4H 3C' : 'flush',
        'AC 2D 9C 3S KD 5S 4D KS AS 4C' : 'straight',  
        'KS AH 2H 3C 4H KC 2C TC 2D AS' : 'three-of-a-kind',
        'AH 2C 9S AD 3C QH KS JS JD KD' : 'two-pairs',
        '6C 9C 8C 2D 7C 2H TC 4C 9S AH' : 'one-pair',
        '3D 5S 2H QD TD 6S KH 9H AD QH' : 'highest-card'
    }

    r = requests.post('localhost/besthand', hand_n_deck_input ) 
    assert r.status_code == 200
    assert json.loads(r.text)

