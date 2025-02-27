import asyncio
import json
from collections import defaultdict

from websockets.asyncio.server import serve

topics = defaultdict(list)


async def handler(websocket):
    print('In handler')
    async for message in websocket:
        print(message)

        json_msg = json.loads(message)

        if 'topic' in json_msg:
            topic = json_msg['topic']
            msg = json_msg['message']

            topics[topic].append(msg)

            print('\n-- TOPIC DICT IS NOW ---')
            print(dict(topics))
            print('------------------------\n')


async def main():
    async with serve(handler, '', 8001) as server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())
