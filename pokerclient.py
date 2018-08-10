import pprint
import json
import aiohttp
import settings

settings.init()
port = settings.config['server']['port']
url = 'http://localhost:{port}/besthand'.format(port=port)


async def get_best_hand_from_server(hand,deck):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=)


def async submit_requests(data):
    for hand_n_deck in data['hand_n_deck_data']:
        hand = pokerhand.Hand.from_string(hand_n_deck['hand'])
        deck = pokerdeck.Deck.from_string(hand_n_deck['deck'])

def get_input_data_from_file(input_file): 
    with open(input_file) as f:
        return json.load(f)
    
if __name__ == "__main__":
    settings.init()
    hand_n_deck_input = get_input_data_from_file('./testdata') 
    pprint.pprint(hand_n_deck_input) 

    #port = args.port if args.port else settings.config['server']['port']
    #await process_input_data(hand_n_deck_input) 

    
