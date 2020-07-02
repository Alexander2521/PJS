from bs4 import BeautifulSoup
import requests
import pandas as pd

print('Please Enter Your Longitude')
x = input()
print('You Chose, ' + x)
print('Please Enter Your Latitude')
y = input()
print('You Chose, ' + y)

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=" + y + "2&lon=" + x + "#.Xv2ujigzY2w")
soup = BeautifulSoup (page.content, 'html.parser')
print(soup.prettify())
