from selenium import webdriver
import zipfile
import requests

try:
    version = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE').text
    url = 'https://chromedriver.storage.googleapis.com/{0}/{1}'.format(version, 'chromedriver_win32.zip')
    r = requests.get(url, allow_redirects=True)
    open('chromedriver.zip', 'wb').write(r.content)
    with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
        zip_ref.extractall()
except:
    pass