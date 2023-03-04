import requests
import pandas as pd

class ColorId:
    def get_color_id():
        orderList = []
        url = "https://atonce.nike.net/search/retailer/0000017835/now"

        querystring = {"avmig":"HO19","childSo":"1000","closeout":"exclude","contracts":"0042270969-1000,0043095513-1000,0042234363-1000,0042258166-1000,0041977603-1000","currency":"USD","extContracts":"none","language":"EN","limit":"400","minAv":"1","page":"1","priceList":"USA","q":"Jordan","region":"USA","sizeType":"USA","so":"1000","soldTo":"0000017835","type":"FTWR"}

        payload = ""
        headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://atonce.nike.net/",
    "Cookie": 'AMCV_B73502BE533095810A490D4C%40AdobeOrg=1075005958%7CMCIDTS%7C19421%7CMCMID%7C12500064053434732880045517027062242948%7CMCAAMLH-1678566079%7C7%7CMCAAMB-1678566079%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1677968479s%7CNONE%7CMCSYNCSOP%7C411-19426%7CvVersion%7C4.4.1; RT="z=1&dm=nike.net&si=e92bd9ff-7157-41a0-bc4c-c13b6d1a2794&ss=leuetfgv&sl=f&tt=pms&bcn=%2F%2F17de4c1a.akstat.io%2F&obo=1&ld=2vlp"; AMCVS_B73502BE533095810A490D4C%40AdobeOrg=1; s_cc=true; s_sq=%5B%5BB%5D%5D; ak_bmsc=71CD29B828B3A4857E6A132BF212D97C~000000000000000000000000000000~YAAQPaosFzrtgKWGAQAA2h9JrhPZYkQ0Nd/7hR98SMbkTCDMoRVG8hv0+30DoPuBOHZ4sa7rwb8XI78lBfOSHdwK6W3ZLy2Ma8Ygtx9WnNSL6JwtloW3YYFsu/oqzC0ax80i3bneN/9lgeOlR3FLvL4X7hOq9QFu2ECLrB9iJwnsjPNv+SPLtyU7KxZ+5wcY5yrVVwMAPrD3s80UjowQht0DrjGjNxhKYmcWm+WQ2hfzsjDF9MgU/Ofr8q+x28m4lZpC8xJOvTpNQ9/Pk4g8k2yFtveZ15tqR504d/IDWBMtggc/wPhCnV2KpNOP3AaWbBEmjbk+VoSUymnUreByU0RuxzlqnX2dxxSETvkBFW08/mVfhzH4QsZo1AciVpY=; bm_sv=A2A8D4C6EF8E37044A54D5670EC36A58~YAAQPaosFzTygKWGAQAAziZLrhOy0vK/3OPXfzSOkyXbmuB8fpplfQSGonq1lm3C/Ow02pcEzcaqhs7U6qTg16D5cSq7tzWZg2fdwhiZuyjqx+JnhqG1FPPjs5Gn+oxQemsYnh0QxIJhtSKe5LG8YJYFq8QV+kT1Dj2UEXffu6QfihbTmABUkayOpqXMoGRFjtymi7HamE7pXTn7YX4l+F1bQBUSjXyJSU7iYfuz+5+WzIvkD2tuAkCBeuj/oew=~1; AUTHSESSION=NGNiY2QxMjAtMDFmYi00NGVlLTliYzctNDM0ZDk0ODIzMTFj; NikeOktaToken=eyJraWQiOiJQQzZ5TTZXRVRuNVZ2ZnpTT0taMzdtVTBYcXBuMDl5OVYtaWZNSzVhamZ3IiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULjdBUUZycmw0aHJ0NDhJZk9WN29ZcG1jVlBjLVZYVllxM3pKM1U5ZXd4RDAub2FyMWV3cWR3bERkZHBjckExdDciLCJpc3MiOiJodHRwczovL25pa2Uub2t0YS5jb20vb2F1dGgyL2F1czI3ejdwNzZhczlEejBIMXQ3IiwiYXVkIjoiaHR0cHM6Ly9uaWtlLm9rdGEuY29tIiwiaWF0IjoxNjc3OTYxMjk4LCJleHAiOjE2Nzc5NjQ4OTgsImNpZCI6Im5pa2UuZ3Rtcy5hdXRoIiwidWlkIjoiMDB1YnhrZDhrc2xiM29MdzUxdDciLCJzY3AiOlsib2ZmbGluZV9hY2Nlc3MiLCJndG1zLnNhbGVzLnVzZXIucmVhZCIsImVtYWlsIiwiZ3Rtcy5zYWxlcy5yZWFkIiwib3BlbmlkIiwicHJvZmlsZSIsImd0bXMuc2FsZXMuY3JlYXRlIiwiZ3Rtcy5zYWxlcy51cGRhdGUiXSwiYXV0aF90aW1lIjoxNjc3OTYxMjk2LCJzdWIiOiJlc3RvcmVAdG9wc2FuZGJvdHRvbXN1c2EuY29tIn0.DpmqnqE6sgyPDzymrbC5fHrXdRi4xx9xBv0cNbMR68UwVmdibazydeJygn1J92amUk7Gkj0r_GPdteVO0ukxzVX2HWSqkQv23PbWAPhtWx3wYk1oOp6DfVuQunM0C5ayPNrpwSph-15XvrscsJZe3JdJtXwTARGFGoPSjIDZmE3JHoqnsem1CQzlezSrAhZUWMpkLhB7YYzMkdxyZYwFjeLiI63XltL_ulogOr_o-USkSVDZezPtaHRegYyBQsb1_dUD4CzC-PYwkB21n0zUXSadrJcUe-WVR6NFuk9RuLCOFmjkgcoYB8H_Covdl22nl7_P4PzlI3SJDY8qIbIZoA; NikeUserToken=eyJraWQiOiIyMzcyN2NkNy0xNmY4LTRhODMtODI1Ni0zM2FlYTI5NmEyY2QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJhdXRoLm5pa2UubmV0Iiwic3ViIjoiZXN0b3JlQHRvcHNhbmRib3R0b21zdXNhLmNvbSIsInNlcyI6IkhnUG1EVSs0LzgvTVlKemVybUVMaVIzeFd4bDZ1M0d6dUJsaTk1eERCK29HVllneldWTmdhRTg1dnZtQWtMU0tSUGFDUFJLUG1uRVQxeEhrNnBOZTdRPT0iLCJ1aWQiOiJhZTgyOGRkNS00MzNhLTQ0MDUtYmUxMy1lMTc3ZjIyY2E4MzgiLCJhc3QiOiIwMDAwMDE3ODM1IiwiZ2F1dGgiOlt7ImF1dGhvcml0eSI6IkRPQy5ST0xFX1VTRVIifSx7ImF1dGhvcml0eSI6IkNMTVIuUk9MRV9VU0VSIn0seyJhdXRob3JpdHkiOiJST0xFX0FVVEhFTlRJQ0FURURfVVNFUlMifSx7ImF1dGhvcml0eSI6IkZVVFIuUk9MRV9VU0VSIn0seyJhdXRob3JpdHkiOiJPU1RQLlJPTEVfVVNFUiJ9LHsiYXV0aG9yaXR5IjoiQVRPTi5ST0xFX0ZVTExfQUNDRVNTIn0seyJhdXRob3JpdHkiOiJPUkRTLlJPTEVfVVNFUiJ9LHsiYXV0aG9yaXR5IjoiV1NBTC5ST0xFX1VTRVIifSx7ImF1dGhvcml0eSI6IkNMTVMuUk9MRV9VU0VSIn0seyJhdXRob3JpdHkiOiJTS1VFLlJPTEVfVVNFUiJ9LHsiYXV0aG9yaXR5IjoiSU5WTi5GVUxMX0FDQ0VTUyJ9XSwibG9jYWxlIjoiZW5fVVMiLCJsdXNlciI6ImVzdG9yZUB0b3BzYW5kYm90dG9tc3VzYS5jb20ifQ.qitxmJ3veFf_xg9Pc2x7C0jEN7XG9V3Cpdo-KwHN4T9e1CFeEZuRO60SIXIUcuhwNMmMl23Rf0QOARJ-zWb3KYYneZmQyX0USaDxdX76yqEZA-IS8r4yRdMbIA-gLfJjIrZE_ZbTu8V_F5GpmeGM6Njn_pYgiQq3mRhCUlKCwhLCYKj3z02_aQXXFlIlPzPL8-GmGObpSP66523Dq9d7F9UMA4O0g8ogd4_g9QeXQaCu3pxeU4nM-atHWU3CjdQSYbP35ey2daFyy_AGCJpGFuBgHPc2cf1h6HADpBLF0ZNNjEymNLty7V0oq0lTI0YKSS9AlSKrtHVjwBWgfL5k3g; NikeOpenToken=T1RLAQLkdcspvXsOZ2ENOH1KLSkAzxY2MRAvv7s9BAVx_pHCOGewn-jXAADwTYOdRupDeVUj3L_TwN9Ilqcyzfgj1-2R-ADblMepuBGHHGiqO2o_qZrTbYm4nX7GIht6kL_q80qgSqJYLbG-4n6gmnAr60hDH1moD1DolLciVDfTeBWoi6UqdY8qw-d8rbLKf1z30z65Xjura6bKq-OBHEjlQMn4Ez2PjEsso3x2udNjreTAOqB53DmZhWIS4JEt2_KtSni_NS5LiVoBB2LGwAQJV0709txqymPtjGK35y4ZYNoGGyvG1FyVDL7BkLQFBUd65xjFnucMYQf38LZz5dqnWAGqCSUiqNe8Ruw8DO4sWHnJMilCkSWwdcmQ; NikeContentToken=exp=1677982900~acl=%2fis%2f*%2fcontent%2f*%21%2fcontent%2f*%21%2fbin%2f*%21%2flibs%2f*%21%2fetc%2f*%21%2fapps%2f*~hmac=61ffe297e0abb7ecbc774e87aac7db88c87fdffb14b4ab99d9866ca2dfbafc36',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
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