from bs4 import BeautifulSoup
import requests as req
from time import sleep
from datetime import datetime

class Publication():
    def __init__(self, authors, jornal, ref, id_article, data, text, title):
        self.list_of_authors = authors
        self.jornal = jornal
        self.article_ref = ref
        self.article_id = id_article
        self.data = data
        self.text = text
        self.title = title

def get_MCID_and_number_of_publications(list_of_terms):
    """This function get MCID data from pubmed and return dictionary in author:MCID format"""
    base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='
    tail = '&usehistory=y&email=michaels17525@mail.ru'
    dict_of_WebEnv = {}
    for el in list_of_terms:
        sleep(2)
        resp = req.get(base + el + tail)
        soup = BeautifulSoup(resp.text, 'xml')
        dict_of_WebEnv[el] = soup.find('WebEnv').text
    return dict_of_WebEnv

def get_articles(list_of_MCID):
    """This function get the dictionary which contains MCID and parse the article data from this MCID to the list of Publication objects"""
    base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&WebEnv="
    tail = "&query_key=1&rettype=abstract"
    temporary_list_of_articles = []
    for el in list_of_MCID.values():
        sleep(2)
        resp = req.get(base + el + tail)
        soup = BeautifulSoup(resp.text, 'xml')
        for article in soup.find_all('PubmedArticle'):
            authors = [last_name.text for last_name in article.find_all('LastName')]
            article_title = article.find('ArticleTitle').text
            if article.find('AbstractText') != None:
                abstract_text = article.find('AbstractText').text
            else:
                abstract_text = 'No valid data'
            if article.find('Title') != None:
                jornal = article.find('Title').text
            else:
                jornal = 'No valid data'
            pubmed_id = article.find('PMID').text
            ref = 'https://pubmed.ncbi.nlm.nih.gov/' + pubmed_id + '/'
            date = article.find('Year').text + " " + article.find('Month').text + " " + article.find('Day').text
            date = datetime.strptime(date, "%Y %m %d")
            temporary_list_of_articles.append(Publication(authors, jornal, ref, pubmed_id, date, abstract_text, article_title))
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
    print(get_articles(dict_of_authors_ref))