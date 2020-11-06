from bs4 import BeautifulSoup
import requests as req

resp = req.get("https://istina.msu.ru/profile/andnadya/")

soup = BeautifulSoup(resp.text, 'lxml')

list_of_a_tags = []
for el in soup.find_all("a"):
    list_of_a_tags.append(el)
    print(el)