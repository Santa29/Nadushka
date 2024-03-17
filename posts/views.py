from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime

from .models import Article, Author


# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'


class ArticlePageView(ListView):
    model = Article
    context_object_name = 'public_list'
    template_name = 'public.html'
    paginate_by = 9

    def get_queryset(self):
        current_year = datetime.now().year
        last_displayed_year = current_year - 10
        sequence_main_author = 1
        queryset = Article.objects.filter(date__year__gte=last_displayed_year, date__year__lte=current_year, authors__sequence_number=sequence_main_author).order_by('-date')
        return queryset


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

    def get_queryset(self):
        queryset = Author.objects.order_by('sequence_number')
        return queryset


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author_detail'


class SearchResultViewSimple(ListView):
    model = Article
    template_name = "search_results.html"
    context_object_name = 'search_list'

    def get(self, request, *args, **kwargs):
        context = {}

        question = self.request.GET.get('q')
        if question != None:
            search_articles = Article.objects.filter(
                Q(name__icontains=question) | Q(abstract__icontains=question)
            ).order_by('-date')

            context['last_question'] = '?q=%s' % question

            current_page = Paginator(search_articles, 9)

            page = request.GET.get('page')
            try:
                context['search_list'] = current_page.page(page)
            except PageNotAnInteger:
                context['search_list'] = current_page.page(1)
            except EmptyPage:
                context['search_list'] = current_page.page(current_page.num_pages)
        return render(request, template_name=self.template_name, context=context)
