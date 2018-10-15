#!/usr/bin/env python3
""" Docstring """
from typing import Tuple

from bs4 import BeautifulSoup


def extract_album_id(html):
    """ Docstring """

    parse_result = BeautifulSoup(html, 'lxml')
    cover = parse_result.find('div', attrs={'id': 'albumCover'})
    album_id = cover['style'].split('/')[-1].split(')')[0].split('.')[0]

    return album_id


def extract_download_links(html):
    """Docstring"""

    parse_result = BeautifulSoup(html, "lxml")
    download_link_element = parse_result.findAll("a", attrs={"class": "dlink"})

    return download_link_element


def extract_album_info(html) -> Tuple[str, str, str, str, str, str]:
    """ Docstring """

    parser = 'lxml'
    table_tag = "table"
    table_attributes = {"id": "album-details"}
    rating_attributes = {"class": "ratingLine"}
    title_tag = "title"
    rating_element = 0
    genre_element = 1
    band_element = 2
    album_element = 3
    year_element = 4
    country_element = 5

    parse_result = BeautifulSoup(html, parser)
    album_table = parse_result.find(table_tag, attrs=table_attributes)

    rating: str = (album_table.findAll("tr")[rating_element]
                   .find("div", attrs=rating_attributes)
                   .get(title_tag)
                   .split(':')[1].lstrip())

    genre: str = (album_table.findAll("tr")[genre_element]
                  .findAll("a")[0]
                  .text)

    band: str = (album_table.findAll("tr")[band_element]
                 .findAll("a")[0]
                 .text)

    album_title: str = (album_table.findAll("tr")[album_element]
                        .find("b")
                        .text)

    year: str = (album_table.findAll("tr")[year_element]
                 .find("a")
                 .text)

    country: str = (album_table.findAll("tr")[country_element]
                    .find("a")
                    .text)

    return rating, genre, band, album_title, year, country
