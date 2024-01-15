import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns = ['actor_id','director_id'])
    actor_director = actor_director.groupby(['actor_id','director_id']).count().reset_index()
    for index , row in actor_director.iterrows():
        if row['timestamp'] >= 3:
            op  = op._append({'actor_id':row['actor_id'],'director_id':row['director_id']},ignore_index = True)
    return op
