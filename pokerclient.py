import asyncio
import pprint
import json
import aiohttp
import settings

settings.init()
port = settings.config['server']['port']
url = 'http://localhost:{port}/besthand'.format(port=port)


async def get_best_hand_from_server(single_play):
    async with aiohttp.ClientSession() as session:
        payload = {'hand_n_deck_data' : [single_play] }
        async with session.get(url, json=payload) as resp:
            #print(await resp.json())
            return await resp.text()


async def submit_requests(data):
    tasks = []
    for hand_n_deck in data['hand_n_deck_data']:
        task = asyncio.ensure_future(get_best_hand_from_server(hand_n_deck))
        tasks.append(task)

    for task in tasks:
        await task
        result = task.result()
        print(result)


def get_input_data_from_file(input_file): 
    with open(input_file) as f:
        return json.load(f)

    
if __name__ == "__main__":
    settings.init()
    hand_n_deck_input = get_input_data_from_file('./testdata') 
    pprint.pprint(hand_n_deck_input) 
    loop = asyncio.get_event_loop() 
    loop.run_until_complete(submit_requests(hand_n_deck_input)) 

    
