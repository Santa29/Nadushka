from bs4 import BeautifulSoup
import requests as req

class Publication():
    list_of_authors = []
    jornal = ''
    ref = ''


def add_to_publications_list(ref):
    resp = req.get(ref)

    soup = BeautifulSoup(resp.text, 'lxml')

    # Count the publications and create the list of empty Publication classes
    for el in soup.find_all("a", href=True):
        if "publication" in el["href"]:
            publication_list_links.append(el["href"])
            print(el["href"])


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

publication_list = []
publication_list_links = []

if __name__ == "main":

    for elem in list_of_referenses_to_parse:
        add_to_publications_list(elem)

    print(publication_list_links)

