import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
import numpy as np
from windrose import WindroseAxes

df = pd.read_csv("windData.csv", parse_dates=['time'])
df = df.set_index('time')

# figure 1: a basic scatter plot with transparency
fig, ax = plt.subplots(figsize=(8, 8), dpi=80)
x0, x1 = ax.get_xlim()
y0, y1 = ax.get_ylim()
ax.set_aspect('equal')
_ = df.plot(kind='scatter', x='speed_x', y='speed_y', alpha=0.35, ax=ax)
plt.savefig('images/figure1.png')

# figure 2: windrose like a stacked histogram with normed (displayed in percent) results
ax = WindroseAxes.from_ax()
ax.bar(df.direction, df.speed, normed=True, opening=0.8, edgecolor='white')
ax.set_legend()
plt.savefig('images/figure2.png')

# figure 3: another stacked histogram representation, not normed, with bins limits
ax = WindroseAxes.from_ax()
ax.box(df.direction, df.speed, bins=np.arange(0, 8, 1))
ax.set_legend()
plt.savefig('images/figure3.png')

# figure 4: a windrose in filled representation, with a controled colormap
ax = WindroseAxes.from_ax()
ax.contourf(df.direction, df.speed, bins=np.arange(0, 8, 1), cmap=cm.hot)
ax.set_legend()
plt.savefig('images/figure4.png')

# figure 5: same as above, but with contours over each filled region
ax = WindroseAxes.from_ax()
ax.contourf(df.direction, df.speed, bins=np.arange(0, 8, 1), cmap=cm.hot)
ax.contour(df.direction, df.speed, bins=np.arange(0, 8, 1), colors='black')
ax.set_legend()
plt.savefig('images/figure5.png')