
# coding: utf-8

# In[1]:


# coding: utf-8

import io, time
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime, timedelta
from sklearn import multioutput, linear_model, ensemble
from sklearn import preprocessing

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable

# Data Visulization

df = pd.read_csv("bj_3_31-4_10.csv") #bj_3_31-4_10.csv
df = df.sort_values(by=["station_id", "time"])
df["station_id"] = df["station_id"].apply(lambda x: x if len(x)<13 else x[0:10]+x[-3:])
df = df.reindex(columns=["id", "station_id", "time", "PM25", "PM10", "O3", "NO2", "CO", "SO2"])
station_df = pd.DataFrame(df.loc[:, ["PM25", "PM10", "O3", "NO2", "CO", "SO2"]].values, index=df.loc[:,:]["time"], dtype=np.float32, columns=["PM25", "PM10", "O3", "NO2", "CO", "SO2"])
print(station_df.head(6))

# df["station_id"] == "dongsi_aq"

plt.figure()
plt.plot(station_df.values)
plt.show()



'''
groups = ["PM25", "PM10", "O3", "NO2", "CO", "SO2"]
i = 1
# plot each column
plt.figure()
for group in groups:
    plt.subplot(len(groups), 1, i)
    plt.plot(station_df.loc[:, group].values)
    plt.title(group, y=0.5, loc="right")
    i += 1
plt.show()

'''


'''
df = pd.read_csv("beijing_17_18_aq.csv")
df = df.sort_values(by=["station_id", "time"])
df["station_id"] = df["station_id"].apply(lambda x: x if len(x)<13 else x[0:10]+x[-3:])
df = df.reindex(columns=["id", "station_id", "time", "PM25", "PM10", "O3", "NO2", "CO", "SO2"])
station_df = pd.DataFrame(df.loc[df["station_id"] == "dongsi_aq", ["PM25", "PM10", "O3", "NO2", "CO", "SO2"]].values, index=df.loc[df["station_id"] == "dongsi_aq",:]["time"], dtype=np.float32, columns=["PM25", "PM10", "O3", "NO2", "CO", "SO2"])
print(station_df.head(6))

groups = ["PM25", "PM10", "O3", "NO2", "CO", "SO2"]
i = 1
# plot each column
plt.figure()
for group in groups:
    plt.subplot(len(groups), 1, i)
    plt.plot(station_df.loc["2017-03-01 01:00:00":"2017-03-31 23:00:00", group].values)
    plt.title(group, y=0.5, loc="right")
    i += 1
plt.show()

groups = ["PM25", "PM10", "O3", "NO2", "CO", "SO2"]
i = 1
# plot each column
plt.figure()
for group in groups:
    plt.subplot(len(groups), 1, i)
    plt.plot(station_df.loc["2017-04-01 01:00:00":"2017-04-30 23:00:00", group].values)
    plt.title(group, y=0.5, loc="right")
    i += 1
plt.show()

groups = ["PM25", "PM10", "O3", "NO2", "CO", "SO2"]
i = 1
# plot each column
plt.figure()
for group in groups:
    plt.subplot(len(groups), 1, i)
    plt.plot(station_df.loc["2017-05-01 01:00:00":"2017-05-31 23:00:00", group].values)
    plt.title(group, y=0.5, loc="right")
    i += 1
plt.show()
'''
