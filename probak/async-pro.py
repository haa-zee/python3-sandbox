#!/usr/bin/env python3
# -*- coding: utf8 -*-
import asyncio
import prctl


async def valami(nev):
    prctl.set_proctitle(nev)
    print(f"{nev} start")
    await asyncio.sleep(10)
    for i in range(2 ** 32):
        prctl.set_proctitle(f"{nev}{i}")
    print(f"{nev} stop")


async def main():
    await asyncio.gather(valami("elso"), valami("masodik"), valami("harmadik"))


if __name__ == "__main__":
    l = asyncio.get_event_loop()
    l.run_until_complete(main())
