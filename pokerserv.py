import os
import os.path
import copy
import json
import argparse
import logging
from aiohttp import web
import settings
import besthandchooser
import pokerhand
import pokerdeck
import util

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

def setup_logger():
    logger = logging.getLogger('pokerserv')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('./logs/pokeserv.log')
    fh.setLevel(logging.DEBUG)
    return logger

def exit_if_still_running():
    pid_file = settings.config['server']['pidfile']

    if not os.path.exists(pid_file):
        return 

    pid = util.get_pid_from_file(pid_file) 

    if pid and util.still_running(pid):
        print('Still Running')
        print('run make stop first')
        sys.exit(0)


def get_args(): 
    parser = argparse.ArgumentParser(description="aiohttp poker server example")
    parser.add_argument('--port')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    settings.init()
    exit_if_still_running()
    app = web.Application()
    app.add_routes([web.get('/besthand', besthand_route)])
    args = get_args()
    port = args.port if args.port else settings.config['server']['port']
    util.log_pid(os.getpid(),settings.config['server']['pidfile'])
    web.run_app(app, port=port)

