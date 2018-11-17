import numpy as np
import requests
from datetime import datetime
import time
import json
import pandas as pd

#GLOBAL VARIABLES

selected_currency='eur'
date_avilable_car="10-10-2018"
car_position='Wieden'
#DATA TO CRITERIA


#DATA

commission='offers.json'
city_list='city.json'
euro='eur'
dollar_u_s='usd'
swiss_franc='chf'
pound_sterling='gbp'



def dowland_data(name_file,name_column=False):#Data segregation function
    with open(name_file) as orders :
        order_lists= json.load(orders)
    segregated_data = pd.DataFrame(order_lists)
    if name_column:
        return   segregated_data[name_column]
    
    return segregated_data




def currency_price(currency):#The function returns the average exchange rate
    if currency=='pl':
        return 1
    else:
        url_1='http://api.nbp.pl/api/exchangerates/rates/a/'
        url_2=currency;
        url_3 = '/'
        url= url_1+url_2+url_3
        response = requests.get(url)
        data = response.json()
        return (data['rates'][0]['mid'])

#CRITERIA


def price_freight():# criterium price freight
    currency=currency_price(selected_currency)
    price=dowland_data(commission,'cena_frachtu')
    new_price=price/currency
    return new_price



def avilable_car(date_avilable):#criterium how many days we must waiting for car 
    list_day=[]
    date_car=datetime.strptime(date_avilable, '%d-%m-%Y')
    
    data_of_receipt = dowland_data(commission,'data_odbioru')
    print(type(data_of_receipt))
    for date in data_of_receipt:
        date_time_obj = datetime.strptime(date, '%d-%m-%Y')
        second=(date_car-date_time_obj).total_seconds()
        day=second/3600/24
        list_day.append(day)
    return pd.DataFrame(list_day,columns=['waiting for a car (day)'])  


# print(avilable_car(date_avilable_car))
def availability():
    profit=np.array(dowland_data(commission,['zysk']))
    capital=np.array(dowland_data(commission,['kapital']))
    asssets=np.array(dowland_data(commission,['aktywa']))
   
    indicator=(profit/capital)*0.1+(profit/asssets)*0.1
    return pd.DataFrame(indicator,columns=['indicator availability'])

# print(availability())


def rating_company():
    positiv=[]
    negative=[]
    neutral=[]
    comments=dowland_data(commission,['komentarze'])
    for index, row in comments.iterrows():
        com=row["komentarze"].partition("/")
        com_two=com[2].partition("/")
        neutral.append(int(com_two[2]))
        negative.append(int(com_two[0]))
        positiv.append(int(com[0]))
    rat_one=np.array(positiv)/(np.array(neutral)+np.array(negative)+np.array(positiv))
    rat_two=np.array(negative)/(np.array(neutral)+np.array(negative)+np.array(positiv))
    rating=rat_one-rat_two
    
    return pd.DataFrame(rating,columns=["raiting_company"])



    # print(positiv)
    # print(negative)
    # print(neutral)
  
# print(rating_company())

def raiting_transrisk():
    rait=dowland_data(commission,"indeks_transrisk")
    return rait


# print(raiting_transrisk())

def distance(position_car):
    city_name=[]
    distance=[]
    id_city_offers=dowland_data(commission,["id_miasto_odbioru"])
    city=dowland_data(city_list,)
    cit_array=np.array(city)
    for index,row in id_city_offers.iterrows():
        for index in cit_array:
            if row[0]==cit_array[index[0]][0]:
                city_name.append(cit_array[index[0]][1])


            
    for name in city_name:

        url_one='https://maps.googleapis.com/maps/api/distancematrix/json?origins= '
        url_car = car_position
        url_two='&destinations= '
        url_cargo=name
        url_three='&mode=driving&language=an'
        url_four="&key="
        api_key ='AIzaSyBysqeWM0PtXWeHxetJnuRMAKdD2mLN39c'
        url = url_one+ url_car + url_two + url_cargo + url_three+url_four+api_key
   
        response = requests.get(url)

        data = response.json()
    
        data=data["rows"][0]["elements"][0]["distance"]["text"]
        data=data.partition(" ")
        data=int(data[0])
        distance.append(data)

    return  pd.DataFrame(distance,columns=["Distance to the load "])
# print(distance(car_position))

