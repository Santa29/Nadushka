from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Post

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

class PublicPageView(TemplateView):
    template_name = 'public.html'

class ContactsPageView(TemplateView):
    template_name = 'contacts.html'

class PublicDetailView(DetailView):
    model = Post
    template_name = 'public_detail.html'
    context_object_name = 'public_detail'