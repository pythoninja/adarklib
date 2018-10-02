#!/usr/bin/env python3
""" Docstring """
from bs4 import BeautifulSoup


def extract_album_id(html):
    """ Docstring """
    soup = BeautifulSoup(html, "lxml")
    cover = soup.find("div", attrs={"id": "albumCover"})
    album_id = cover["style"].split("/")[-1].split(")")[0].split(".")[0]

    return album_id
