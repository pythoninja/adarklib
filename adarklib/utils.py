#!/usr/bin/env python3
""" Collection of useful functions """
import asyncio

import aiohttp

from adarklib.client import fetch_album


def generate_header() -> dict:
    """ Generates header for HTTP request """

    origin = "http://dark-world.ru"
    accept_encoding = "gzip, deflate"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)" \
                 "Chrome/66.0.3359.181 YaBrowser/18.6.0.2255 Yowser/2.5 Safari/537.36"
    content_type = "application/x-www-form-urlencoded"
    accept = "text/html"
    referer = "http://dark-world.ru"
    x_requested_with = "XMLHttpRequest"
    connection = "keep-alive"

    return {
        "Origin": origin,
        "Accept-Encoding": accept_encoding,
        "User-Agent": user_agent,
        "Content-Type": content_type,
        "Accept": accept,
        "Referer": referer,
        "X-Requested-With": x_requested_with,
        "Connection": connection
    }


async def create_session() -> aiohttp.ClientSession:
    """ Creates aiohttp.ClientSession and returns it """

    headers = generate_header()

    client_session = aiohttp.ClientSession(headers=headers)
    return client_session


async def task_runner(urls):
    """ Docstring """
    client_session = await create_session()

    async with client_session as session:
        tasks = [asyncio.create_task(fetch_album(session, url)) for url in urls]

        return await asyncio.gather(*tasks)
