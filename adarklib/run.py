#!/usr/bin/env python3
""" Docstring """
# import aiohttp
import asyncio
import os

print(os.getcwd())


async def generate_header():
    """ Docstring """
    # origin = ""
    # accept_encoding = ""
    # user_agent = ""
    # content_type = ""
    # accept = ""
    # referer = ""
    # x_requested_with = ""
    # connection = ""

    return {
        "Origin": "http://dark-world.ru",
        "Accept-Encoding": "gzip, deflate",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/66.0.3359.181 YaBrowser/18.6.0.2255 Yowser/2.5 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html",
        "Referer": "http://dark-world.ru",
        "X-Requested-With": "XMLHttpRequest",
        "Connection": "keep-alive",
    }


async def p1_f():
    """ Docstring """
    await asyncio.sleep(2)
    h_var = await generate_header()
    print(h_var)


async def p2_f():
    """ Docstring """
    print("p2")


async def main():
    """ Docstring """
    print("i am in async coro")
    await asyncio.gather(p2_f(), p1_f())


asyncio.run(main(), debug=True)
