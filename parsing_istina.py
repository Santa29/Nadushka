from bs4 import BeautifulSoup
import requests as req

resp = req.get("https://istina.msu.ru/profile/andnadya/")

soup = BeautifulSoup(resp.text, 'lxml')

list_of_a_tags = []
list_of_publications = []
list_of_authors = []
list_of_jornals = []
for el in soup.find_all("a", href=True):
    list_of_a_tags.append(el)

i=-1
for el in list_of_a_tags:
    print(el.text)
    if "publications" in el.text:
        list_of_publications.append(el)
        i+=1
    elif "workers" in el.text:
            list_of_authors[i].append(el)
    elif "jornals" in el.text:
        list_of_jornals.append(el)
print(list_of_authors, list_of_jornals, list_of_publications)
