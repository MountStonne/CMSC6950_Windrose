import pandas as pd
import numpy as np
from math import pi

df = pd.read_csv("windRawData.csv", parse_dates=['time'])
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