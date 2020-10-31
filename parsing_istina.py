from bs4 import BeautifulSoup
import requests as rq
import lxml

page = rq.get("https://istina.msu.ru/profile/andnadya/")
soup = BeautifulSoup(page.text, 'lxml')
print(soup)