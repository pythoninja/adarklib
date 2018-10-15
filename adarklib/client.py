#!/usr/bin/env python3
"""
Asynchronous client for dark-world.ru website
"""
from typing import Dict

import aiohttp

from adarklib.models import Album
from adarklib.parsers import extract_album_id
from adarklib.parsers import extract_album_info
from adarklib.parsers import extract_download_links


async def fetch_album(session: aiohttp.ClientSession, url: str) -> Album:
    """ Docstring """

    async with session.get(url=url) as resp:
        response = await resp.text()

        album_id = extract_album_id(response)

    rating, genre, band, title, year, country = extract_album_info(html=response)

    links = await get_download_links(session, album_id)

    album = Album(
        genre=genre,
        band=band,
        title=title,
        year=year,
        country=country,
        links=links,
        rating=rating,
        url=url)

    # print(album)

    return album


async def get_download_links(session: aiohttp.ClientSession, album_id: int):
    """ Docstring """

    show_albums_link: str = 'http://dark-world.ru/links/show/albums/'
    post_data: Dict[str, int] = {'ajax': 1}

    post_url: str = f'{show_albums_link}/{album_id}'

    async with session.post(post_url, data=post_data) as resp:
        result: str = await resp.text()

        raw_links = extract_download_links(html=result)

        parsed_links = []

        if len(raw_links) > 1:
            for link in raw_links:
                parsed_links.append(f'http://dark-world.ru{link["href"]}')
            return parsed_links
        else:
            return f'http://dark-world.ru{raw_links[0]["href"]}'
