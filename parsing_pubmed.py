from bs4 import BeautifulSoup
import requests as req
import time

class Publication():
    def __init__(self, list, jornal, ref, id_article, data):
        self.list_of_authors = list
        self.jornal = jornal
        self.article_ref = ref
        self.article_id = id_article
        self.data = data

def get_MCID_and_number_of_publications(list_of_terms):
    base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='
    tail = '&usehistory=y&email=michaels17525@mail.ru'
    dict_of_WebEnv = {}
    for el in list_of_terms:
        time.sleep(2)
        resp = req.get(base + el + tail)
        soup = BeautifulSoup(resp.text, 'xml')
        dict_of_WebEnv[el] = [soup.find('WebEnv').text, soup.find('Count').text]
    return dict_of_WebEnv

def get_articles(list_of_MCID):
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&WebEnv="
    tail = "&query_key=1&rettype=abstract"
    temporary_list_of_articles = []
    ids = []
    data = []
    title = []
    for el in list_of_MCID.keys():
        time.sleep(2)
        resp = req.get(base + el[0] + tail)
        soup = BeautifulSoup(resp.text, 'xml')
        temporary_list_of_articles.append(soup)
        authors = []
        jornals = []
        title.append((soup.find_all('ArticleTitle')).text.split())
        ids.append((soup.find_all('PMID')).text.split())
        data.append((soup.find_all('DateRevised')).text.split())
        for i in range(int(el[1])):
            pass
    return temporary_list_of_articles

def connect_to_db_and_read_data():
    pass

def update_the_db():
    pass

def update_log_file():
    pass

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
    dict_of_authors_ref = get_MCID_and_number_of_publications(list_of_referenses_to_parse)
    print(dict_of_authors_ref)