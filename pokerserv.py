import copy
import json
import argparse
from aiohttp import web
import besthandchooser
import pokerhand
import pokerdeck

class PEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,pokerhand.Hand):
            return str(obj)
        return json.JSONEncoder.default(self,obj)

def prehandler(handler):
    async def new_handler(request):
        try:
            data = await request.json()
        except Exception as e:
            return web.json_response(status=400,text=json.dumps({ 'status' : 'error' }))
        return await handler(data)

    return new_handler

@prehandler
async def besthand_route(data):

    response_hands = []

    for hand_n_deck in data['hand_n_deck_data']:
        hand = pokerhand.Hand.from_string(hand_n_deck['hand'])
        deck = pokerdeck.Deck.from_string(hand_n_deck['deck']) 

        best_hand_chooser = besthandchooser.BestHandChooser(hand,deck)

        best_hand = best_hand_chooser.get_best_hand()

        response_hands.append({ 'hand' : hand_n_deck['hand'] , 
                                'deck' : hand_n_deck['deck'] , 
                                'best_hand' : best_hand })

    ret = {'hands' : response_hands}
    return web.json_response(text=json.dumps(ret, cls=PEncoder))


def get_args(): 
    parser = argparse.ArgumentParser(description="aiohttp poker server example")
    parser.add_argument('--port')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    app = web.Application()
    app.add_routes([web.post('/besthand', besthand_route)])
    args = get_args()
    web.run_app(app, port=args.port)

