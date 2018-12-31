#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import websockets
import random
import sys
import os


async def ws_test():
    while True:
        try:
            ws = await websockets.connect('ws://localhost:8765')
            message = "{} {}".format(os.getpid(), str(random.random()))
            await ws.send(message)
            reply = await ws.recv()
            if message != reply:
                print("Eltér!! {} vs {}".format(message, reply))
                sys.exit(-1)
        finally:
            await ws.close()


if __name__ == "__main__":
    # asyncio.get_event_loop().run_until_complete(ws_test())
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(ws_test())
    loop.run_forever()
