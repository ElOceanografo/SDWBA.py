import scipy as sp
from sdwba import *
import pandas as pd

data = pd.read_csv("../data/generic_krill_Conti2006.csv")
krill = Scatterer(data.x, data.y, data.z, data.a, data.g, data.h)

r0 = krill.r
krill.rotate(tilt=45)

krill.reset_rotation()
assert (krill.r == r0).all()

