#!/usr/bin/env python3
""" Docstring """
import asyncio

import aiohttp

from adarklib.parsers import extract_album_id
from adarklib.parsers import extract_download_links
from adarklib.utils import create_session


async def fetch_html(session: aiohttp.ClientSession, url: str):
    """ Docstring """

    async with session.get(url=url) as resp:
        response = await resp.text()

        album_id = extract_album_id(response)

    links = await get_download_links(session, album_id)

    await print_result(status=f'Download link for {resp.url}', links=links)


async def get_download_links(session: aiohttp.ClientSession, album_id: int):
    """ Docstring """

    show_albums_link = 'http://dark-world.ru/links/show/albums/'

    async with session.post(f"{show_albums_link}/{album_id}", data={'ajax': 1}) as resp:

        result = await resp.text()

        links = extract_download_links(html=result)

        return links


async def print_result(status, links):
    """ Docstring """

    print(f'{status}: {links}')
    # print(links)

    # if len(download_link_element) > 1:
    #     for link in download_link_element:
    #         return f'http://dark-world.ru{link["href"]}'
    #         print(f'http://dark-world.ru{link["href"]}')
    # else:
    #     return f'http://dark-world.ru{download_link_element[0]["href"]}'
    # return download_link_element[0]["href"]


async def main():
    """ Docstring """
    client_session = await create_session()

    urls = (
        'http://dark-world.ru/albums/Deicide-Overtures-Of-Blasphemy.php',
        'http://dark-world.ru/albums/Hren-Pole-Chudes-V-Strane-Durakov.php',
        'http://dark-world.ru/albums/Korpiklaani-Kulkija.php',
        'http://dark-world.ru/albums/Bathsheba-Servus.php'
    )

    async with client_session as session:
        tasks = [asyncio.create_task(fetch_html(session, url)) for url in urls]

        await asyncio.gather(*tasks)


asyncio.run(main(), debug=True)
