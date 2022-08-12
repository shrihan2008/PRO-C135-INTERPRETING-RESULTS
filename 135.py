
import pandas as pd
import csv
import matplotlib.pyplot as plt
f=pd.read_csv('star_with_gravity.csv')
mass=f['Mass'].to_list()
radius =f['Radius'].to_list()
d =f['Distance'].to_list()
g =f['Gravity'].to_list()
name =f['Star_name'].to_list()

plt.plot(name, d)
plt.plot(name, g)
plt.plot(name, radius)
plt.plot(name, mass)