# Project 1: Web Crawler

## Description

## Requirements

  - Python 3.6+
  - [Scrapy](https://github.com/scrapy/scrapy)
    - Method 1 (quickest): `$pip install scrapy`
    - Method 2 (anaconda): `$conda install -c conda-forge scrapy`
  - [w3lib](https://github.com/scrapy/w3lib)
    - Method 1 (quickest): `$pip install w3lib` 
    - Method 2 (anaconda): `conda install -c anaconda w3lib` 
  - [extruct](https://github.com/scrapinghub/extruct)
    - (quickest): `$pip install extruct`
  - [BeautifulSoup](https://github.com/wention/BeautifulSoup4)
    - (quickest): `$pip install bs4`
  - [urlopen](https://pypi.org/project/urlopen/)
    - (quickest): `$pip install urlopen`

## Installation

  1. Open a terminal in the *Code* directory
  2. Change directory: `$cd scrapy_crawler/spiders`
  3. Launch crawler in terminal: `$scrapy crawl freeman --logfile freeman.log`
  3. Launch crawler in terminal (saves custom data parameters): `$scrapy crawl freemanmoore --logfile freemanmoore.log -O freemanmoore.jl`
