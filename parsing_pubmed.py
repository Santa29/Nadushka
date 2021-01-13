from bs4 import BeautifulSoup
import requests as req
import time

class Publication():
    list_of_authors = []
    jornal = ''
    ref = ''
    article_id = ''
    article_url = ''

def get_MCID(list_of_terms):
    base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='
    tail = '&usehistory=y&email=michaels17525@mail.ru'
    dict_of_WebEnv = {}
    for el in list_of_terms:
        time.sleep(2)
        resp = req.get(base + el + tail)
        soup = BeautifulSoup(resp.text, 'xml')
        dict_of_WebEnv[el] = soup.find('WebEnv').text
    return dict_of_WebEnv



list_of_referenses_to_parse = [
    "Andrianova+NV",
    "Popkov+VA",
    "Babenko+VA",
    "Silachev+DN",
    "Pevzner+IB",
    "Zorova+LD",
    "Zorov+SD",
    "plotnikov+EY",
    "Brezgunova+AA"
]

dict_of_authors_ref = {}

publication_list = []
publication_list_links = []

if __name__ == "__main__":
    dict_of_authors_ref = get_MCID(list_of_referenses_to_parse)
    print(dict_of_authors_ref)