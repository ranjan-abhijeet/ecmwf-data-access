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


# Day for which we want to download data. It usually takes 5-6 days
# for ECMWF to upload data. Hence, keep the date atleast 5 days earlier than
# current date.

def met_data_downloader(year, month, day, data_download_path):

    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
            'product_type': 'reanalysis',
            'format': 'grib',
            'pressure_level': '1000',
            'variable': [
                '10m_u_component_of_wind', '10m_v_component_of_wind', 
                '2m_temperature', 'boundary_layer_height',
            ],
            'year': year,
            'month': month,
            'day': day,
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
        f'{data_download_path}/{year}_{month}_{day}.grib')

    # xarray used to open .grib files
    ds = xr.open_dataset(f'{data_download_path}/{year}_{month}_{day}.grib')

    # this loop will print the variables or columns available in data along with their units.
    for v in ds:
        print("{}, {}, {}".format(v, ds[v].attrs["long_name"], ds[v].attrs["units"]))

    # converts the xarray to dataframe
    df = ds.to_dataframe()
    
    # converts the dataframe to .csv
    df.to_csv(f'{data_download_path}/{year}_{month}_{day}.csv')