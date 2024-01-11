import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views.drop_duplicates(inplace=True)
    selected_rows = views[views['author_id'] == views['viewer_id']]
    selected_rows_df = selected_rows[['author_id']].rename(columns={'author_id': 'id'})
    selected_rows_df.sort_values(by='id', inplace=True)
    selected_rows_df.drop_duplicates(subset='id', keep='first', inplace=True)
    return selected_rows_df