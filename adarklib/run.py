#!/usr/bin/env python3
""" Docstring """
import asyncio

import aiohttp
from bs4 import BeautifulSoup

from adarklib.parsers import extract_album_id
from adarklib.utils import create_session


async def fetch_html(session: aiohttp.ClientSession, url: str):
    """ Docstring """

    async with session.get(url=url) as resp:
        response = await resp.text()

        print(f'Extracting download links from {resp.url}')

        album_id = extract_album_id(response)

    await extract_download_links(session, album_id)


async def extract_download_links(session: aiohttp.ClientSession, album_id: int):
    """ Docstring """

    show_albums_link = 'http://dark-world.ru/links/show/albums/'

    async with session.post(f"{show_albums_link}/{album_id}", data={'ajax': 1}) as resp:

        result = await resp.text()

        parse_result = BeautifulSoup(result, "lxml")

        download_link_element = parse_result.findAll("a", attrs={"class": "dlink"})

        if len(download_link_element) > 1:
            for link in download_link_element:
                print(f'http://dark-world.ru{link["href"]}')
        else:
            print(f'http://dark-world.ru{download_link_element[0]["href"]}')


async def main():
    """ Docstring """
    client_session = await create_session()

    urls = (
        'http://dark-world.ru/albums/Deicide-Overtures-Of-Blasphemy.php',
        'http://dark-world.ru/albums/Hren-Pole-Chudes-V-Strane-Durakov.php'
    )

    async with client_session as session:
        tasks = [asyncio.create_task(fetch_html(session, url)) for url in urls]

        await asyncio.gather(*tasks)


asyncio.run(main(), debug=True)
