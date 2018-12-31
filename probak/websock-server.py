#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' websockets demo
Egy echo szerver, ami semmi mást nem csinál, csak visszaküldi a kapott üzenetet
Amiért íródott: kíváncsi vagyok, mi történik, ha párhuzamosan több kliens "bombázza" üzenetekkel?

Update: sajnos közben arra is rá kellett jönnöm, hogy eme szerver működéséből adódóan
nem lehet azt csinálni, hogy több kliens végtelen ciklusban küldözgeti az üzeneteit, a kapcsolat
lezárása nélkül, mivel a szerver fogad egy üzenetet, visszaküldi, majd megszűnik.
'''
import asyncio
import websockets


async def server(websocket, path):
    message = await websocket.recv()
    print("WS: {}   Path: {}    Message: {}".format(websocket, path, message))
    await websocket.send(message)


if __name__ == "__main__":
    start_server = websockets.serve(server, 'localhost', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
