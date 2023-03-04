import requests
import pandas as pd

class ColorId:
    def get_color_id():
        orderList = []
        url = "https://atonce.nike.net/search/retailer/0000017835/now"

        querystring = {"avmig":"HO19","childSo":"1000","closeout":"exclude","contracts":"0042270969-1000,0043095513-1000,0042234363-1000,0042258166-1000,0041977603-1000","currency":"USD","extContracts":"none","language":"EN","limit":"400","minAv":"1","page":"1","priceList":"USA","q":"Jordan","region":"USA","sizeType":"USA","so":"1000","soldTo":"0000017835","type":"FTWR"}

        payload = ""
        headers = { #add your Headers here}
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        # print(response.text)
        for items in response.json()['products']:
            styleColorCode = items['styleColorCode']
            data = {
                "Styles": styleColorCode
            }
            orderList.append(data)
        df = pd.DataFrame(orderList)
        return df
