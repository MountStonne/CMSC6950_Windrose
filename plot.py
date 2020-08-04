import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
from windrose import WindroseAxes

df = pd.read_csv("https://www.smartatlantic.ca/erddap/tabledap/SMA_st_johns_wharf.csv?time%2Cwind_spd_avg%2Cwind_dir_avg&time%3E=2019-08-01T00%3A00%3A00Z&time%3C=2020-07-31T23%3A59%3A59Z", parse_dates=['time'])
df = df.set_index('time')

# A basic scatter plot with transparency
fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.set_aspect('equal')
_ = df.plot(kind='scatter', x='speed_x', y='speed_y', alpha=0.35, ax=ax)
plt.savefig('figure1.png')