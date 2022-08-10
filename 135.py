from turtle import distance
import pandas as pd
import plotly.express as px
import csv

f=pd.read_csv('a.csv')
mass=f['Mass'].to_list()
radius =f['Radius'].to_list()
d =f['Distance'].to_list()
g =f['Unnamed: 0'].to_list()
name =f['Star_name'].to_list()
fig=px.scatter(y=name,x=d)
fig.show()

fig1=px.scatter(y=name,x=mass)
fig1.show()

fig2=px.scatter(y=name,x=g)
fig2.show()

fig3=px.scatter(y=name,x=radius)
fig3.show()