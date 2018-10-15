#!/usr/bin/env python3
""" Docstring """
import asyncio
from typing import Iterable

from adarklib.models import AlbumSchema
from adarklib.utils import task_runner


def downloader(urls=None, output=None, save_to=None):
    """ Docstring """
    if urls and isinstance(urls, Iterable):
        info = asyncio.run(task_runner(urls), debug=True)
        # info = await main(urls)

        schema = AlbumSchema()
        # print(schema)

        result = schema.dumps(info, many=True, indent=2, ensure_ascii=False)

        print(result)
    else:
        print("urls should be passed and must")
