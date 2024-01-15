import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates()
    activities = activities.groupby('sell_date')['product'].agg(['nunique', lambda x: ','.join(sorted(set(x)))]).reset_index()
    activities.columns=['sell_date','num_sold','products']
    activities.sort_values(by='num_sold',ascending = False)
    return activities
    