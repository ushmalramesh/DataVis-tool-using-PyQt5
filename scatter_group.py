import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.pyplot import figure
import sys

def plot(filename):
    df = pd.read_csv(filename)
    ls= df.groupID.unique()
    d={}
    for i in ls:
        d[i]=data=df.loc[df['groupID']== i]
    figure(num=None, figsize=(10, 18), dpi=80, facecolor='w', edgecolor='k')
    start = 321
    add = 0
    for i in ls:
        df1 = d[i].loc[d[i]['parent'].isnull()]
        df2 = d[i].loc[d[i]['parent'].notnull()]

        df1['time'] = df1['time'].apply(lambda x: datetime.strptime(x.split('T')[0].replace('-', ' '), "%Y %m %d"))
        t0 = min(df1['time'])
        df1['time'] = df1['time'].apply(lambda x: (x - t0).days)

        df2['time'] = df2['time'].apply(lambda x: datetime.strptime(x.split('T')[0].replace('-', ' '), "%Y %m %d"))
        t0 = min(df2['time'])
        df2['time'] = df2['time'].apply(lambda x: (x - t0).days)

        x = df1['time'].values
        y = df1['textchars']

        p = df2['time'].values
        q = df2['textchars']

        val = start + add

        ax = plt.subplot(val)
        group = str(i)
        ax.set_title('Group: ' + group)
        plt.scatter(x, y, s=4)
        plt.scatter(p, q, s=4)
        plt.xlabel('Time in days', fontsize=10)
        plt.ylabel('Length of text', fontsize='medium')
        plt.legend(['First Posts','Replies'])
        add = add + 1
    plt.suptitle("Submission time vs text length - Topic based comparison")
    plt.show()
