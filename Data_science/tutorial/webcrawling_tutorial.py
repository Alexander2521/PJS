# https://www.dataquest.io/blog/web-scraping-tutorial-python/
# https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.Xv2ujigzY2w
# 유튜브 : 당신의 종합코딩 펫, 힟콛 Subscribe

from bs4 import BeautifulSoup
import requests
import pandas as pd

# Step 3 :  parsing weather data from NWS
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup (page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
# print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
# print(period)
# print(short_desc)
# print(temp)
img = tonight.find("img")
desc = img['title']
# print(desc)
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
# print(periods)

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
# print(short_descs)
# print(temps)
# print(descs)

weather = pd.DataFrame({
    "period": periods,
    "short_desc": short_descs,
    "temp": temps,
    "desc": descs
})
print(weather)

temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
print(temp_nums)

print(round(weather["temp_num"].mean(),2))

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
print(is_night)

# working, but not efficient
# x = (weather["temp_num"].mean())
# y = round(x, 2)
# print(y)

# ## Step 2 : distinguish by className
# page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
# print(page.status_code)
# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup.prettify())
#
#
# print(soup.select("div p"))
# # print(soup.find_all('p', class_='outer-text'))
# # print(soup.find_all(id="first"))

## Step 1. first web crawling
# page = requests.get ("http://dataquestio.github.io/web-scraping-pages/simple.html")
# # print(page)
# print(page.status_code)
# # print(page.content)
# soup = BeautifulSoup(page.content, 'html.parser')
# # print(soup.prettify())
# # print( list(soup.children) )
# # html = list(soup.children)[2]
# # print(list(html.children))
# # body = list(html.children)[3]
# # print(list(body.children))
# # p = list(body.children)[1]
# # print(p.get_text())
#
# print(soup.find_all('p'))
#
# print(soup.find_all('p')[0].get_text())
