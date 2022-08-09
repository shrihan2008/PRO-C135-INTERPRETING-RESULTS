from turtle import distance
import pandas as pd
import matplotlib as plt
import plotly.express as px
import csv

f=pd.read_csv('a.csv')
mass=f['Mass'].to_list()
radius =f['Radius'].to_list()
d =f['Distance'].to_list()
g =f['Unnamed'].to_list()
name =f['Star_name'].to_list()
fig=px.scatter(x=name,y=d)
fig.show()

fig1=px.scatter(x=name,y=mass)
fig1.show()

fig2=px.scatter(x=name,y=g)
fig2.show()

fig3=px.scatter(x=name,y=radius)
fig3.show()