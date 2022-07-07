#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cdsapi
import time

start = time.time()

c = cdsapi.Client()

c.retrieve("reanalysis-era5-pressure-levels",
    {
        "variable": "temperature",
        "pressure_level": "1000",
        "product_type": "reanalysis",
        "date": "2022-06-01/2022-06-07",
        "format": "grib"
    }, "test.grib")

end = time.time()
print(f"[+] Time to process {round(end-start,3)} seconds")