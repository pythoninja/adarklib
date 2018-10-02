#!/usr/bin/env python3
""" Docstring """
import aiohttp


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


async def create_session():
    """ Docstring """

    headers = generate_header()

    client_session = aiohttp.ClientSession(headers=headers)
    return client_session
