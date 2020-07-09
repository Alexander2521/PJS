from bs4 import BeautifulSoup

import requests
import pandas as pd




print("#####################")
print('Please Enter Your Longitude')
x = input()
print('You Chose, ' + x)
print('Please Enter Your Latitude')
y = input()
print('You Chose, ' + y)

page = requests.get("h\ttps://forecast.weather.gov/MapClick.php?lat=" + y + "&lon=" + x )
# page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup (page.content, 'html.parser')
# print(soup.prettify())

seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
img = tonight.find("img")
desc = img['title']
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
test = temps.str.extract("(?P<temp_num>\d+)", expand=False)

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)

print(round(weather["temp_num"].mean(),2))
