from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import json
import pandas as pd

def make_heatmap(filename):
    sns.set(rc={'axes.facecolor':'lightgray', 'figure.facecolor':'lightgray'})
    df = pd.read_csv(filename)

    df['time']=df['time'].apply(lambda x: datetime.strptime(x.split('T')[0].replace('-',' '),"%Y %m %d"))
    t0 = min(df['time'])
    df['time']=df['time'].apply(lambda x: (x-t0).days)
    df = df[df['parent'].isnull()]

    df2 = pd.DataFrame(columns=["topicID", "day", "number_of_posts"])
    row = 0
    for day in df['time']:
        smaller_df = df[df['time'] == day]
        for topic_ID in smaller_df['topicID']:
            smallest_df = smaller_df[smaller_df['topicID'] == topic_ID]
            df2.loc[row] = [topic_ID, day, len(smallest_df)]
            row += 1
    df2 = df2.drop_duplicates().reset_index()
    df2['number_of_posts'] = pd.to_numeric(df2['number_of_posts'], errors='coerce')
    df2['day'] = pd.to_numeric(df2['day'], errors='coerce')

    data = df2.pivot("topicID", "day", "number_of_posts")

    return data


def plot(data):
    f, ax = plt.subplots(figsize=(9, 6))

    sns.heatmap(data,annot=False, fmt="f", linewidths=.5, ax=ax,cmap="hot")
    plt.title("Heatmap of post count by Topic ID")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    make_heatmap('2017-5-5.csv')