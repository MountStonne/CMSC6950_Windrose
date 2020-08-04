import pandas as pd
import numpy as np
from math import pi

df = pd.read_csv("https://www.smartatlantic.ca/erddap/tabledap/SMA_st_johns_wharf.csv?time%2Cwind_spd_avg%2Cwind_dir_avg&time%3E=2019-08-01T00%3A00%3A00Z&time%3C=2020-07-31T23%3A59%3A59Z", parse_dates=['time'])
df = df.rename(columns={
    'wind_spd_avg' : 'speed',
    'wind_dir_avg' : 'direction',
})
df = df.set_index('time')
df = df.drop(['UTC'])
df = df.astype('float64')

df['speed_x'] = df['speed'] * np.sin(df['direction'] * pi / 180.0)
df['speed_y'] = df['speed'] * np.cos(df['direction'] * pi / 180.0)

df.to_csv('windData.csv', index = True)