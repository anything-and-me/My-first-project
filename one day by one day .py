import requests
import datetime
import json
from selenium import webdriver


def weather():
    weather = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=长沙')
    data = json.loads(weather.text)
    weather_date = data['data']['forecast'][0]['type']
    return weather_date


def time():
    day = datetime.datetime.now()
    today = day.date()
    return today


def words():
    driver = webdriver.PhantomJS('D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
    driver.get("https://www.baidu.com")

    inputd = driver.find_element_by_css_selector('#kw')
    inputd.send_keys("")

    button = driver.find_element_by_css_selector('#su')
    button.click()


weather_date = weather()
today = time()

words()
print(f'''
Today is {today}.
The weather is {weather_date}.
                                            -----punch card love your day
'''.format(today, weather_date))
