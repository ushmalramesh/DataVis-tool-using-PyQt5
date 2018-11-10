from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import json,numpy
import pandas as pd

def read_data(filename):
    df = pd.read_csv(filename)
    topics = df.topicID.unique()
    df['time']=df['time'].apply(lambda x: datetime.strptime(x.split('T')[0].replace('-',' '),"%Y %m %d"))
    df['topicID'] = df['topicID'].apply(lambda x: int(x))
    topic_dict = {}
    for topic in topics:
        topic_df = df[df['topicID']==topic]
        t0 = min(topic_df['time'])
        topic_dict[topic]=t0
    timelist = []
    for i in range(len(df)):
        timelist.append((df.loc[i]['time'] - topic_dict[df.loc[i]['topicID']]).days)
    df3 = pd.DataFrame(columns=['day'])
    df3['day']=timelist
    df['time']=df3['day']
    cols = ['user', 'topic','day']
    #cols.extend(topics)
    df2 = pd.DataFrame(columns = cols)
    df = df[df['parent'].isnull()]
    users = list(set(df['user']))
    row = 0
    for user in users:
        smaller_df = df[df['user'] == user]
        for i in range(len(topics)):
            entry = [user]
            entry.append(topics[i])
            if int(topics[i]) in list(smaller_df['topicID']):
                smallest_df = smaller_df[smaller_df['topicID'] == topics[i]]
                entry.append(min(smallest_df['time']))
                df2.loc[row] = entry
                row += 1

    return df2

def plot(df2):
    df2.topic = df2.topic.astype(float)
    df2.day = df2.day.astype(float)
    g = sns.catplot(x="topic", y="day", kind="violin", inner=None, data=df2)
    sns.swarmplot(x="topic", y="day", color="k", size=3, data=df2, ax=g.ax)
    plt.title("Violin plot showing the submission behaviour of a set of users by topic")
    plt.show()

