import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns = ['name', 'population','area'])
    for index, row in world.iterrows():
        if row['area'] >= 3000000 or row['population'] >= 25000000:
            op = op._append({'name': row['name'], 'population': row['population'], 'area': row['area']}, ignore_index = True)
    return op