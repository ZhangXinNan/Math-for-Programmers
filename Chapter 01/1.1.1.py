import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


ys = [30]
xs = range(0, 501)
np.random.seed(seed=42)
for delta in np.random.normal(0, 0.5, 500):
    ys.append(ys[-1] + delta)

plt.plot(ys)
plt.ylabel('Stock Price ($)')
plt.xlabel('Elapsed Time (min)')
plt.savefig('figures/1.01.svg')


r = stats.linregress(xs,ys)
line = [r.slope * x + r.intercept for x in xs]
std = np.std([(y-y0) for y,y0 in zip(ys,line)])
top = [y + std for y in line]
bottom = [y - std for y in line]
plt.plot(xs,ys)
plt.plot(xs,line)
plt.plot(xs,top)
plt.plot(xs,bottom)
plt.ylabel('Stock Price ($)')
plt.xlabel('Elapsed Time (min)')
plt.savefig('figures/1.02.svg')
plt.savefig('figures/1.03.svg')