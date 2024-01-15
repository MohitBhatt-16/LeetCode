import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    df = activity.groupby('player_id').min().reset_index()
    df.drop(columns=['device_id','games_played'],inplace = True)
    df.rename(columns ={'event_date':'first_login'},inplace = True)
    return df
    