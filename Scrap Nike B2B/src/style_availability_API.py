import requests
import pandas as pd

class ColorId:
    def get_color_id():
        orderList = []
        url = "https://atonce.nike.net/search/retailer/0000017835/now"
        #Fill your own Query string
        querystring = {"avmig":"","childSo":"","closeout":"","contracts":"","currency":"","extContracts":"","language":"","limit":"","minAv":"","page":"","priceList":"","q":"Jordan","region":"","sizeType":"","so":"","soldTo":"","type":""}

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
        # print(response.text)
        for items in response.json()['products']:
            styleColorCode = items['styleColorCode']
            data = {
                "Styles": styleColorCode
            }
            orderList.append(data)
        df = pd.DataFrame(orderList)
        return df
