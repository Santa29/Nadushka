from bs4 import BeautifulSoup
import requests as req

class Publication():
    list_of_authors = []
    jornal = ''
    ref = ''


list_of_referenses_to_parse = [
    "https://istina.msu.ru/profile/andnadya/",
    "https://istina.msu.ru/profile/popkov-v/",
    "https://istina.msu.ru/profile/BabenkoVA/",
    "https://istina.msu.ru/profile/SilachevDN/",
    "https://istina.msu.ru/profile/Pevzner_IB/",
    "https://istina.msu.ru/profile/lju/",
    "https://istina.msu.ru/profile/zorov/",
    "https://istina.msu.ru/profile/pleg/",
    "https://istina.msu.ru/profile/brezgunova/"
]

dict_of_authors_ref = {
    "/workers/60585830/": "andNadya"
}

resp = req.get("https://istina.msu.ru/profile/andnadya/")

soup = BeautifulSoup(resp.text, 'lxml')

list_of_a_tags = []
for el in soup.find_all("a", href=True):
    list_of_a_tags.append(el)


i = 0
for el in list_of_a_tags:
    if "publications" in el['href']:
        i+=1
publication_list = []
for public in range(i):
    publication_list.append(Publication())


counter = -1
for el in list_of_a_tags:
    if "publications" in el['href']:
        counter+=1
        publication_list[counter].ref = el['href']
    elif "workers" in el['href'] and "style" not in el['href']:
        publication_list[counter].list_of_authors.append(el['href'])
    elif "jornals" in el["href"]:
        publication_list[counter].jornal = el['href']

for el in publication_list:
    print(el.ref + '\n')
    print(el.jornal)
    el.list_of_authors = set(el.list_of_authors)
    print(el.list_of_authors)