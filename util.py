from dotenv import dotenv_values
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

def get_api_key():
    '''
    This is a helper function to retrieve to openweathermap API key 
    from a.env file

    parameter: No parameter
    Return vaue: an Api Key
    Return Type: string
    '''
    config = dict(dotenv_values('.env'))
    api_key = config.get('API_KEY')
    

    return api_key

def adjust_date(row):
    '''
    This is a helper function to convert a unix datetime to a utc datetime,
    while factoring in the timezone offset

    parameters: A dataFrame row
    Return value:  A utc datetime
    Return Type a datetime
    '''
    actual_unix_date = row['unix_date'] - row['unix_timezone']

    #convert to utc datetime
    utc_date = datetime.fromtimestamp(actual_unix_date)

def get_engine():
    '''
    This is a function that retrieves connetion credentials from
    a .env file and returns a postgres sqlalchemy engine

    parameter: None
    Return value: A sqlalchemy engine
    Return Type: A SQLalchemy engine object
    '''
    config = dict(dotenv_values('.env'))
    db_username = config.get('DB_USERNAME')
    db_password = config.get('DB_PASSWORD')
    db_host = config.get('DB_HOST')
    db_port = config.get('DB_PORT')
    db_name = config.get('DB_NAME')
    

    engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')
    
    return engine

