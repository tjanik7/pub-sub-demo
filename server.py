import asyncio

from websockets.asyncio.server import serve
from websockets.sync.client import connect


async def handler(websocket):
    async for message in websocket:
        print(message)
        await websocket.send(f'You sent "{message}"')


async def main():
    async with serve(handler, '', 8001) as server:
        await server.serve_forever()


# def send():
#     uri = 'ws://localhost:8001'
#     with connect(uri) as websocket:
#         msg = input('Msg to send:')
#
#         websocket.send(msg)


if __name__ == '__main__':
    asyncio.run(main())
