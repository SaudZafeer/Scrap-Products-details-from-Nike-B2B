import requests
import pandas as pd
from style_availability_API import *

def get_product_name(Styles):
        url = "https://atonce.nike.net/product/"

        querystring = {"childSo":"1000","contracts":"0042270969-1000,0043095513-1000,0042234363-1000,0042258166-1000,0041977603-1000","currency":"USD","hzn":"60","language":"EN","limit":"400","priceList":"USA","region":"USA","sizeType":"USA","so":"1000","soldTo":"0000017835","styleColor":{Styles},"withAv":"false"}

        payload = ""
        #Fill your headers in order to run this code
        headers = {
    "User-Agent": "",
    "Accept": "",
    "Accept-Language": "",
    "Accept-Encoding": "",
    "Connection": "",
    "Referer": "https://atonce.nike.net/",
    "Cookie": '',
    "Sec-Fetch-Dest": "",
    "Sec-Fetch-Mode": "",
    "Sec-Fetch-Site": ""
}

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        for item in response.json():
            styleID = item['styleColor']
            for items in item['languages']:
                name = items['name']
                Gender = items['nameSec']
        print(name,Gender)
        return name,Gender




def GetProductData(Styles):
        appended = []
        url = "https://atonce.nike.net/availability/sales/1000/availability"
        querystring = {"productIds":{Styles}}

        payload = ""
        #Fill your headers in order to run this code
        headers = {
    "User-Agent": "",
    "Accept": "",
    "Accept-Language": "",
    "Accept-Encoding": "",
    "Connection": "",
    "Referer": "https://atonce.nike.net/",
    "Cookie": '',
    "Sec-Fetch-Dest": "",
    "Sec-Fetch-Mode": "",
    "Sec-Fetch-Site": ""
}

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        name,Gender = get_product_name(Styles)
        for product in response.json():
            id = product['productId']
            for item in product['productAvailabilities']:
                Season = item['distributionCenter']['name']
                print(Season)
                for item2 in item['availabilities']:
                    for size_no in item2['sizes']:
                        code = size_no['code']
                        quantities = size_no['quantity']
                        print(id,code,quantities)
                        data = {
                            "name" : name,
                            "Available in": Season,
                            "ID": id,
                            "Gender": Gender,
                            "sizes": code,
                            "Quantities": quantities
                        }
                        appended.append(data)
        return appended


df = ColorId.get_color_id()
mainDataList = []
for Styles in df['Styles']:
    print(Styles)
    lst = GetProductData(Styles)
    mainDataList.append(lst)

dfs = []
for d in mainDataList:
    df = pd.DataFrame(d)
    dfs.append(df)
result_df = pd.concat(dfs)
result_df.to_csv('Availale product Details.csv',index=False)
