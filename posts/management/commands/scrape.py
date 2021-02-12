from django.core.management.base import BaseCommand

from bs4 import BeautifulSoup
import requests as req
from time import sleep
from datetime import datetime
from posts.models import Article, Author

class Publication():
    def __init__(self, authors, jornal, ref, id_article, data, text, title):
        self.list_of_authors = authors
        self.jornal = jornal
        self.article_ref = ref
        self.article_id = id_article
        self.data = data
        self.text = text
        self.title = title

class Command(BaseCommand):
    list_of_referenses_to_parse = [
    "Andrianova+NV",
    "Popkov+VA",
    "Babenko+VA",
    "Silachev+DN",
    "Pevzner+IB",
    "Zorova+LD",
    "Zorov+SD",
    "Plotnikov+EY",
    "Brezgunova+AA"
    ]

    dict_of_authors_ref = {}

    def get_MCID_and_number_of_publications(self, list_of_terms):
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

    def create_link(self, list_of_authors, article_to_create_link):
        """This function create the link between article and authors which contains in the database"""
        Author.objects.all()
        for el in list_of_authors:
            try:
                Author.objects.get(name=el)
            except:
                pass

    def get_articles(self, list_of_MCID):
        """This function get the dictionary which contains MCID and parse the article data from this MCID to the list of Publication objects"""
        base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&WebEnv="
        tail = "&query_key=1&rettype=abstract&email=michaels17525@mail.ru"
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
