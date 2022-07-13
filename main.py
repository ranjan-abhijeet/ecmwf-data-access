"""
publishing_delay: Number of days it takes ECMWF to publish the data. Varies from 
                    5 to 6 days based on when you are querying the data. For
                    safer side, it is set to 6 days.

data_download_path: The path where .grib file will be downloaded from the ECMWF server
                    and CSV file will be generated
"""

import os
from datetime import datetime, timedelta
from time import time
from tracemalloc import start
from turtle import down
from meteorological_data_downloader import met_data_downloader

def download(publishing_delay, data_download_path):
    start_day = datetime.now() - timedelta(days=publishing_delay)

    year = start_day.strftime("%Y")
    month = start_day.strftime("%m")
    day = start_day.strftime("%d")
    met_data_downloader(year, month, day, data_download_path)

data_download_path = "/home/abhijeet/Ranjan/Data/ECMWF_data"

try:
    download(5, data_download_path)
except Exception as e:
    print("[-] Data not published, downloading latest available data")
    download(6, data_download_path)