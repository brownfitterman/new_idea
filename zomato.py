from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

from places_info import get_info
driver=webdriver.Chrome("chromedriver.exe")
driver.get('https://www.zomato.com/bangalore/drinks-and-nightlife?zomato_place_v2=17104')


while True:
    try:
        if driver.find_element(By.XPATH,'//*[@id="root"]/div/div[176]/div/div[1]/h3').text == "End of search results":
            break
    except:
        pass
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
all=driver.find_elements(By.XPATH,'//*[@id="root"]/div/div/div/div/div/div')

data=[]
for i in all:
    try:
        print(f"getting   {i.find_element(By.XPATH,'a[2]/div[1]/h4').text}")
        place_name=i.find_element(By.XPATH,'a[2]/div[1]/h4').text
        address=i.find_element(By.XPATH,'a[2]/p').text.split(",")[0]
        data.append(get_info(place_name,address))
        # place_image.append(i.find_element(By.XPATH,'a[1]/div[2]/img').get_attribute('src'))
        # rating.append(i.find_element(By.XPATH,'a[2]/div[1]/div/div/div/div/div/div[1]').text)
    except:
        pass

populartimess=[]
timewaits=[]
ratings=[]
ratings_n=[]
current_popularitys=[]
time_spents=[]
typess=[]
priceRanges=[]
Addresss=[]
descs=[]
tels=[]
lats=[]
lngs=[]
googleMapLocations=[]
facebookLinks=[]
placeNames=[]
timeZones=[]
neighborhoods=[]
avgTimeSpents=[]
zipcodes=[]
f=open("main.txt", "w") 
f.write(data)
for item in data:
    populartimess.append(item['TotalBusyHour'])
    timewaits.append(item['timewait'])
    ratings.append(item["Rating"])
    ratings_n.append(item["Rating_n"])
    current_popularitys.append(item["CurrentPopularity"])
    time_spents.append(item["TimeSpent"])
    typess.append(item["Types"])
    priceRanges.append(item["PriceRange"])
    Addresss.append(item["Address"])
    descs.append(item['Description'])
    tels.append(item["PhoneNumber"])
    lats.append(item["Latitude"])
    lngs.append(item["Longitude"])
    googleMapLocations.append(item["GoogleMapLocation"])
    facebookLinks.append(item['FacebookLink'])
    placeNames.append(item["PlaceName"])
    timeZones.append(item["TimeZone"])
    neighborhoods.append(item["Neighborhood"])
    avgTimeSpents.append(item["AverageTimeSpent"])
    avgTimeSpents.append(item['ZipCode'])

df=pd.DataFrame({"TotalBusyHour": populartimess or "",
        "timewait": timewaits,
        "Rating" : ratings,
        "Rating_n" : ratings_n,
        "CurrentPopularity" : current_popularitys,
        "TimeSpent" : time_spents,
        "Types":typess,
        "PriceRange":priceRanges,
        "Address": Addresss,
        "Description":descs,
        "PhoneNumber": tels,
        "Latitude": lats,
        "Longitude": lngs,
        "GoogleMapLocation": googleMapLocations,
        "FacebookLink" : facebookLinks,
        "PlaceName" : placeNames,
        "TimeZone": timeZones,
        "Neighborhood" : neighborhoods,
        "AverageTimeSpent":avgTimeSpents,
        "ZipCode": zipcodes
        })

df.to_csv("demo_bangalore.csv")
