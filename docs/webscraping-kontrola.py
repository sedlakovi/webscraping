import base64
import gzip
import io
import sys

if sys.version_info[0] < 3:
        print("Je potřeba nainstalovat Python 3. :-(")
        sys.exit(1)

import pandas as pd
import os

import notebook

import requests
from bs4 import BeautifulSoup

import scrapy


response = requests.get("https://www.sedlakovi.org/webscraping/verification.html")
response.raise_for_status()

html = response.text

dataframe = pd.read_html(html)[0]

print()
print("Tabulka stažená z webu")
print("======================")
print()
print(dataframe)
print()
print()
print("A heslo kurzu zní:")
print("------------------")
soup = BeautifulSoup(html, features="lxml")
print(soup.select_one("#heslo-kurzu").text)
