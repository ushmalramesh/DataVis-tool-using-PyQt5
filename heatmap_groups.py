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

    df2 = pd.DataFrame(columns = ["group", "day" , "number_of_posts"])
    row = 0
    for day in df['time']:
        smaller_df = df[df['time'] == day]
        for group in smaller_df['groupID']:
            smallest_df = smaller_df[smaller_df['groupID'] == group]
            df2.loc[row] = [group, day, len(smallest_df)]
            row += 1
    df2 = df2.drop_duplicates().reset_index()
    df2['number_of_posts']= pd.to_numeric(df2['number_of_posts'], errors='coerce')
    df2['day']= pd.to_numeric(df2['day'], errors='coerce')

    data = df2.pivot("group", "day" , "number_of_posts")
    return data

def plot(data):
    f, ax = plt.subplots(figsize=(9, 6))

    sns.heatmap(data,annot=False, fmt="f", linewidths=.5, ax=ax,cmap="hot")
    plt.title("Heatmap of post count by Group")
    plt.legend()
    plt.show()