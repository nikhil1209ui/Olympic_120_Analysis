import pandas as pd
import numpy as np

df_athletes1 = pd.read_csv('athlete_events_1.csv')
df_athletes2 = pd.read_csv('athlete_events_2.csv')
df_athletes = pd.concat([df_athletes1, df_athletes2], ignore_index=True)

df_noc = pd.read_csv('noc_regions.csv')


def preprocess():
    global df_athletes, df_noc

    df_athletes = df_athletes[df_athletes['Season'] == 'Summer']
    df = df_athletes.merge(df_noc, on='NOC', how='left')
    df.drop_duplicates(inplace=True)
    df = pd.concat([df, (pd.get_dummies(df['Medal'], dtype='int'))], axis=1)

    return df
