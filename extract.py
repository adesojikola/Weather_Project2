import pandas as pd
from util import get_engine
from transform import GetReport

def extract_uscities(file):
    '''
    This is a function to extract US cities
    from an excel files including the contains longitude and latitudes

    parameters:
    - file - an xlsx file

    Return values: a pandas dataFrame object
    Return Type: a pandas dataFrame
    '''
    df = pd.read_excel(file)

    return df

def extract_dbcities(table_name):
    '''
    This is a function to extract US cities longitude and latitudes
    from the database.

    parameters:


    Return values: a pandas dataFrame object
    Return Type: a pandas dataFrame
    '''
    engine = get_engine()
    df = pd.read_sql_table(table_name, engine)
    df = df[['city']].head(20)
    
    return df

def extract_weather(df):
    '''
    This is a function to extract current weather conditions of cities
    from all locations on a file from the openweathermap API.
    The contains longitude and latitudes

    parameters:
        - df - cities
    Return values: a pandas dataFrame object
    Return Type: a pandas dataFrame
    '''
        #initialize an empty list to hold the rows
    rows = []

    for index, row in df.iterrows():
        city = row['city']
        weather_data =GetReport(city)
        weather_data.getResponse()
        data = weather_data.getData()
        rows.append(data)
    
    weather_df = pd.DataFrame(rows)

    return weather_df
