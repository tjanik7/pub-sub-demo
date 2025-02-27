import json

from websockets.sync.client import connect

uri = 'ws://localhost:8001'


def send_as_client():
    with connect(uri) as websocket:
        msg = input('Msg to send: ')
        d = {
            'topic': 'sports',
            'message': msg
        }

        websocket.send(json.dumps(d))


if __name__ == '__main__':
    while True:
        send_as_client()
