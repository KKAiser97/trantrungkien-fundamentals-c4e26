from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

city=input("Enter a city:")
url="https://wind.waqi.info/nsearch/full/{}?n=4".format(city)
con=urlopen(url)
raw_data=con.read()
page_content=raw_data.decode("utf8")
soup=BeautifulSoup(page_content,"html.parser")
aqi=json.loads(page_content)
air=aqi["results"]

for i in air:
    print("location:",i["s"]["n"][0])
    print("time:",i["s"]["t"][0])
    print("AQI:",i["s"]["a"])
    

