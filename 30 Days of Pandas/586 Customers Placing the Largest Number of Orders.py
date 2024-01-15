import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    op = orders.groupby(['customer_number']).count().reset_index()
    op.sort_values(by='order_number',ascending = False,inplace = True)
    return op[['customer_number']][0:1]