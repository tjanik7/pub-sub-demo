import asyncio

from websockets.sync.client import connect
from websockets.asyncio.server import serve

uri = 'ws://localhost:8001'


async def handler(websocket):
    async for message in websocket:
        print(message)


async def s():
    async with connect(uri) as websocket:
        async for message in websocket:
            print(message)


def send_as_client():
    with connect(uri) as websocket:
        msg = input('Msg to send: ')

        websocket.send(msg)

        greeting = websocket.recv()
        print(f'Response: {greeting}')


if __name__ == '__main__':
    while True:
        send_as_client()
