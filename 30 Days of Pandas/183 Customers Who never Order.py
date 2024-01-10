import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    cust_order = customers.join(orders.set_index('customerId'), on='id', how='outer', rsuffix='_order')
    selected_customers = cust_order[cust_order['id_order'].isnull()]
    return selected_customers[['name']].rename(columns = {'name':'Customers'})
    