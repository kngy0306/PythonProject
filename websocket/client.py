import asyncio
import websockets

async def hello():
  async with websockets.connect('ws://localhost:2222') as websocket:
    await websocket.send('Hello World!')
    print(await websocket.recv())

asyncio.run(hello())