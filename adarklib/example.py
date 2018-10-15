#!/usr/bin/env python3
""" Docstring """
# import asyncio
from adarklib.download import downloader

URLS = (
    # 'http://dark-world.ru/albums/Deicide-Overtures-Of-Blasphemy.php',
    # 'http://dark-world.ru/albums/Hren-Pole-Chudes-V-Strane-Durakov.php',
    # 'http://dark-world.ru/albums/Korpiklaani-Kulkija.php',
    # 'http://dark-world.ru/albums/Bathsheba-Servus.php',
    # 'http://dark-world.ru/albums/Elderwind-Chem-Holodnee-Noch.php',
    # 'http://dark-world.ru/albums/Sirenia-Arcane-Astral-Aeons.php',
    # 'http://dark-world.ru/albums/Severoth-When-The-Night-Falls.php',
    # 'http://dark-world.ru/albums/Pure-Wrath-Ascetic-Eventide.php',
    # 'http://dark-world.ru/albums/Brothers-Of-Metal-Prophecy-Of-Ragnaroek.php',
    # 'http://dark-world.ru/albums/Rienaus-Aamutaehdelle.php',
    # 'http://dark-world.ru/albums/Rienaus-Saatanalle.php',
    # 'http://dark-world.ru/albums/Uratsakidogi-Black-Hop.php',
    'http://dark-world.ru/albums/Odor-Mortis-Tam-Gde-Pout-Vetra-Demo.php',
    'http://dark-world.ru/albums/Odor-Mortis-Spasi-I-Otsosi-Demo.php'
)


# async def run():
#     await downloader(urls=urls, output='json', save_to='output.json')

downloader(urls=URLS, output='json', save_to='output.json')

# asyncio.run(run())
