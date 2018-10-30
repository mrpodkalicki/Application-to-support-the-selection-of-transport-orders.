import numpy
import requests
from datetime import datetime
import time
import json
import random
import pandas as pd

#DANE DO KRYTERIW POBIERANIE
oferty='example.json'
miasta='miasta.json'


def pobierz_dane(nazwa_pliku):
    with open(nazwa_pliku) as zlecenia:
        lista_zlecen = json.load(zlecenia)
    wszystkie_dane = pd.DataFrame(lista_zlecen)
    return wszystkie_dane





def cena_frachtu(rodzaj_waluty,cena_frachtu):
    url_1='http://api.nbp.pl/api/exchangerates/rates/a/'
    url_2=rodzaj_waluty;
    url_3 = '/'
    url= url_1+url_2+url_3
    response = requests.get(url)
    data = response.json()
    return (data['rates'][0]['mid'])



print(cena_waluty('eur'))
#
# #kryteriA
# def odleglosc(pol_auta,pol_ladunku):
#     #https: // maps.googleapis.com / maps / api / distancematrix / json?origins = Boston, MA | Charlestown, MA & destinations = Lexington, MA | Concord, MA & departure_time = now & key = YOUR_API_KEY
#     url_1='https://maps.googleapis.com/maps/api/distancematrix/json?origins='
#     url_pol_auta = pol_auta
#     url_2='&destinations='
#     url_pol_ladunku=pol_ladunku
#     url_3='&mode=driving&sensor=false'
#
#    # klucz_api ='AIzaSyCcRQGm-nURxtwy5pR5etpoi102l-cC-dE'
#     url = url_1 + url_pol_auta + url_2 + url_pol_ladunku + url_3
#     #print(url)
#     response = requests.get(url)
#
#     data = response.json()
#     #kilometry=data['rows'][0]['elements'][0]['value']
#     print(data)
#     #return data
#
#
# #def cena(cena,waluta):
# def czas_oczekiwania(lista_year, lista_month, lista_day): #zrobione
#     mac = []
#     #year = int(input('Podaj aktualny rok (np. 2018): '))
#     #month = int(input('Podaj aktaulny miesiac (1-12): '))
#     #day = int(input('Podaj aktualny dzien (1-31): '))
#     for i in range(len(DATY)):
#        # car = datetime(int(year), int(month), int(day))
#         car = datetime(2018, 1, 1)
#         cargo = datetime(int(lista_year[i]), int(lista_month[i]), int(lista_day[i]))
#         lista_cargo.append(cargo)
#         sec =(cargo - car).total_seconds()
#         day = sec/3600/24
#         mac.append(day)
#     return(mac)
#
# tescik3=crit_time(lista_year, lista_month, lista_day)




