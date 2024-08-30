from util import get_engine, get_api_key
from extract import  extract_uscities, extract_dbcities, extract_weather
from load import load_data

def main():
    engine = get_engine()
    api_key = get_api_key()
    print(api_key)

     #extract the cities
    df_cities = extract_uscities(file='uscities.xlsx')
    print('US Cities Data Extracted Successfully')

    #load cities data to postgres
    df_cities.to_sql('cities', engine, if_exists='append', index=False)
    print('US Cities Data loaded Successfully into Database')


    #extract the cities
    df_cities= extract_dbcities(table_name='cities')
    print('US Cities Data Extracted Successfully from the Database')

    '''
    This is a function to extract current weather conditions of cities
    from all locations using longitude and latitudes on a file from the openweathermap API.
    '''
    
    weather_df = extract_weather(df_cities)
    print('Weather Data for different cities in US Extracted Successfully')


    #load data to postgres
    load_data(df = weather_df, engine=engine, table='weather')
    print('Data loaded Successfully')

if __name__== '__main__':
    main()
    print('Pipeline run successfully')




    