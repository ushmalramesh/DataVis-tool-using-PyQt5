from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import json,numpy
import pandas as pd
#sns.set(rc={'axes.facecolor':'lightgray', 'figure.facecolor':'lightgray'})
def read_data(filename):
    df = pd.read_csv(filename)
    groups = df.groupID.unique()
    df['time']=df['time'].apply(lambda x: datetime.strptime(x.split('T')[0].replace('-',' '),"%Y %m %d"))
    t0 = min(df['time'])
    df['time']=df['time'].apply(lambda x: (x-t0).days)
    cols = ['user', 'group','day']
    #cols.extend(topics)
    df2 = pd.DataFrame(columns = cols)
    df = df[df['parent'].isnull()]
    users = list(set(df['user']))
    row = 0
    for user in users:
        smaller_df = df[df['user'] == user]
        groups = smaller_df.groupID.unique()
        for group in groups:
            entry = [user]
            entry.append(group)
            smallest_df = smaller_df[smaller_df['groupID'] == group]
            entry.append(min(smallest_df['time']))
            df2.loc[row] = entry
            row += 1
    df2.group = df2.group.astype(float)
    df2.day = df2.day.astype(float)
    return df2

def plot(df2):
    g = sns.catplot(x="group", y="day", kind="violin", inner=None, data=df2)
    sns.swarmplot(x="group", y="day", color="k", size=3, data=df2, ax=g.ax);
    plt.title("Violin Plot showing distribution of First Posts among Groups")
    plt.show()


