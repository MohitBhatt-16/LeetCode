import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    op = pd.DataFrame(columns=['product_id'])
    for index, row in products.iterrows():
        if row['low_fats'] == "Y" and row['recyclable'] == "Y":
            op = op._append({'product_id':row['product_id']}, ignore_index = True)
    return op
    