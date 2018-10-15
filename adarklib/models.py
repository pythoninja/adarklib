#!/usr/bin/env python3
""" Module which describes Album class and JSON model """
from marshmallow import fields
from marshmallow import post_dump
from marshmallow import post_load
from marshmallow import pre_load
from marshmallow import Schema


class Album:
    """ Docstring """

    def __init__(self, genre, band, title, year, country, links, rating, url):
        """ Docstring """

        self._genre = genre
        self._band = band
        self._title = title
        self._year = year
        self._country = country
        self._links = links
        self._rating = rating
        self._url = url

    def __repr__(self):
        """ Docstring """

        return (f'{self.__class__.__name__}'
                f'(genre={self._genre},'
                f' band={self._band},'
                f' album={self._title},'
                f' year={self._year},'
                f' country={self._country},'
                f' download_links={self._links},'
                f' rating={self._rating},'
                f' url={self._url})')

    @property
    def genre(self):
        """ Docstring """
        return self._genre

    @property
    def band(self):
        """ Docstring """
        return self._band

    @property
    def title(self):
        """ Docstring """
        return self._title

    @property
    def year(self):
        """ Docstring """
        return self._year

    @property
    def country(self):
        """ Docstring """
        return self._country

    @property
    def download_links(self):
        """ Docstring """
        return self._links

    @property
    def rating(self):
        """ Docstring """
        return self._rating

    @property
    def url(self):
        """ Docstring """
        return self._url


class AlbumSchema(Schema):
    """ Docstring """

    style = fields.Str()
    band = fields.Str()
    album = fields.Str()
    year = fields.Int()
    country = fields.Str()
    download_links = fields.List(fields.Str())
    rating = fields.Int()
    url = fields.Str()

    @pre_load(pass_many=True)
    def unwrap_envelope(self, data, many):
        """ Docstring """

        key = '_albums' if many else '_album'
        return data[key]

    @post_dump(pass_many=True)
    def wrap_with_envelope(self, data, many):
        """ Docstring """

        key = '_albums' if many else '_album'
        return {key: data}

    @post_load
    def make_album(self, data):
        """ Docstring """

        return Album(**data)
