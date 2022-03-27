
import sys
sys.path.append('../Chapter 03')
import numpy as np
import matplotlib.pyplot as plt
from draw3d import *

triangle = [(2.3,1.1,0.9), (4.5,3.3,2.0), (1.0,3.5,3.9)]

draw3d(
    Polygon3D(*triangle),
    Points3D(*triangle),
    axes=False,
    origin=False
)
plt.savefig('figures/1.08.svg')

