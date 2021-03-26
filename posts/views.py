from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.core.paginator import Paginator


from .models import Article, Author

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'
    
class AboutPageView(TemplateView):
    template_name = 'about.html'

class ResourcePageView(TemplateView):
    template_name = 'resource.html'

class StructurePageView(TemplateView):
    template_name = 'structure.html'

class HistoryPageView(TemplateView):
    template_name = 'history.html'

class ModelPageView(TemplateView):
    template_name = 'model.html'

class ArticlePageView(ListView):
    model = Article
    context_object_name = 'public_list'
    template_name = 'public.html'

class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'public_detail.html'
    context_object_name = 'public_detail'

class AuthorsListView(ListView):
    model = Author
    template_name = 'authors.html'
    context_object_name = 'authors_list'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author_detail'