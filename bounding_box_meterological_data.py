"""
Libraries to install:
1. cdsapi -- conda install -c conda-forge cdsapi
2. xarray -- conda install -c anaconda xarray

Getting the API and adding it to path (Windows OS):
    -- https://www.ecmwf.int/en/computing/software/ecmwf-web-api
    -- https://confluence.ecmwf.int/display/CKB/How+to+install+and+use+CDS+API+on+Windows

"""
import cdsapi
import xarray as xr
c = cdsapi.Client()

# Day for which we want to download data. It usually takes 5-6 days
# for ECMWF to upload data. Hence, keep the date atleast 5 days earlier than
# current date.

year = 2022
month = 7
day = 1
c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'grib',
        'pressure_level': '1000',
        'variable': [
            'divergence', 'fraction_of_cloud_cover', 'geopotential',
            'ozone_mass_mixing_ratio', 'potential_vorticity', 'relative_humidity',
            'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_humidity',
            'specific_rain_water_content', 'specific_snow_water_content', 'temperature',
            'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity',
            'vorticity', 'boundary_layer_height'
        ],
        'year': str(year),
        'month': str(month),
        'day': str(day),
        'time': [
            '00:00', '01:00', '02:00',
            '03:00', '04:00', '05:00',
            '06:00', '07:00', '08:00',
            '09:00', '10:00', '11:00',
            '12:00', '13:00', '14:00',
            '15:00', '16:00', '17:00',
            '18:00', '19:00', '20:00',
            '21:00','22:00', '23:00'
        ],
        # area: it is the bounding box which for which we want to download data.
        # here it is set as latitiude_top, longitude_left, latitude_bottom, longitude_right
        'area': [
            38, 68, 8, 98
        ],
    },
    # 'india.grib' is the file in which data is downloaded.
    'india.grib')

# xarray used to open .grib files
ds = xr.open_dataset('india.grib')

# this loop will print the variables or columns available in data along with their units.
for v in ds:
    print("{}, {}, {}".format(v, ds[v].attrs["long_name"], ds[v].attrs["units"]))

# converts the xarray to dataframe
df= ds.to_dataframe()

# converts the dataframe to .csv
df.to_csv('india.csv')