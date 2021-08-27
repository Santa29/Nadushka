from django.core.management.base import BaseCommand

from posts.models import Article, Author

from bs4 import BeautifulSoup
import requests as req
from time import sleep
from datetime import datetime

class Publication():
    def __init__(self, authors, jornal, ref, id_article, data, text, title):
        self.list_of_authors = authors
        self.journal = jornal
        self.article_ref = ref
        self.article_id = id_article
        self.date = data
        self.text = text
        self.title = title

class Command(BaseCommand):
    list_of_referenses_to_parse = []

    dict_of_authors_ref = {}

    def create_list_of_references(self, list_of_referenses_to_parse):
        """Create the list which contains all of the authors in the db in special format to search them in pubmed db"""
        for author in Author.objects.all():
            temp = author.lastname + '+' + author.firstname[0] + author.thirdname[0]
            list_of_referenses_to_parse.append(temp)
        return list_of_referenses_to_parse

    def get_MCID_and_number_of_publications(self, list_of_terms):
        """This function get MCID data from pubmed and return dictionary in author:MCID format"""
        base = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term='
        tail = '&usehistory=y&email=michaels17525@mail.ru'
        dict_of_WebEnv = {}
        for el in list_of_terms:
            sleep(1)
            resp = req.get(base + el + tail)
            soup = BeautifulSoup(resp.text, 'xml')
            dict_of_WebEnv[el] = soup.find('WebEnv').text
        return dict_of_WebEnv

    def create_link(self, article_to_create_link):
        """This function create the link between article and authors which contains in the database"""
        try:
            base = Article.objects.get(istina_article_id = article_to_create_link.article_id)
            for author in article_to_create_link.list_of_authors:
                try:
                    base.authors.add(Author.objects.get(slug=author))
                    base.save()
                except:
                    pass
        except:
            pass
    
    def create_articles(self, articles):
        "This function create and update the articles from BD"
        for el in articles:
            try:
                Article.objects.update_or_create(
                    istina_article_id = el.article_id,
                    defaults = dict(
                        name = el.title,
                        date = el.date.strftime("%Y-%m-%d"),
                        url = el.article_ref,
                        journal = el.journal,
                        abstract = el.text,
                    )
                )
            except:
                pass

    def get_articles(self, list_of_MCID):
        """This function get the dictionary which contains MCID and parse the article data from this MCID to the list of Publication objects"""
        base = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&WebEnv="
        tail = "&query_key=1&rettype=abstract&email=michaels17525@mail.ru"
        temporary_list_of_articles = []
        for el in list_of_MCID.values():
            sleep(1)
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
    
    def handle(self, *args, **options):
        self.list_of_referenses_to_parse = self.create_list_of_references(self.list_of_referenses_to_parse)
        temp = self.get_MCID_and_number_of_publications(self.list_of_referenses_to_parse)
        list_of_articles = self.get_articles(temp)
        self.create_articles(list_of_articles)
        for el in list_of_articles:
            self.create_link(el)