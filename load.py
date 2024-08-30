import pandas as pd



def load_data(df, engine, table):
    '''
    This is a function that loads data to a table on postgres database

    parameters:
    - df - a dataFrame
    - engine - a sqlalchemy engine
    - table - databae table on postgress
    Return value: Null
    Return Type: Null
    '''
    df.to_sql(table, con=engine, if_exists='append', index=False)