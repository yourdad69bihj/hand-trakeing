import asyncio
import websockets
import json

async def handler(websocket):
    print("Phone Connected to PCVR Bridge")
    async for message in websocket:
        data = json.loads(message)
        # This is where the data enters your PC.
        # You can now route this to SlimeVR or VRChat via OSC.
        print(f"Tracking Hips at: {data['hips']['x']}, {data['hips']['y']}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8080):
        print("Waiting for phone on port 8080...")
        await asyncio.future()

asyncio.run(main())