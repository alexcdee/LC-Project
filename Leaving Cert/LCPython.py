from pandas import *
dataIn = read_csv("data.csv")

steps = dataIn['steps'].tolist()
print(steps)
light = dataIn['light'].tolist()
print(light)
time = dataIn['time'].tolist()
print(time)

import statistics
import matplotlib.pyplot as plt

plt.plot(steps,light,time)
plt.show()

