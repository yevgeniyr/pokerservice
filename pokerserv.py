import argparse
from aiohttp import web
import card

async def besthand_route(request):
    data = await request.json()

    response_hands = []

    for hand_n_deck in data['hand_n_deck_data']:
        best_hand = card.best_hand(hand_n_deck) 

        response_hands.append( { 'hand' : hand_n_deck['hand'] , 
                                 'deck' : hand_n_deck['deck'] , 
                                 'best_hand' : best_hand } )

    return web.json_response( { 'hands' : response_hands })


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


