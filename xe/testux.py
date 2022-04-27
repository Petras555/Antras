# from selenium import webdriver
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options

from requests_html import HTMLSession

session = HTMLSession()

url = "https://www.elektrum.lt/lt/namams/elektra"

r = session.get(url)

r.html.render()