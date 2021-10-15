from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('public/', views.ArticlePageView.as_view(), name = 'public'),
    path('contacts/', views.ContactsPageView.as_view(), name = 'contacts'),
    path('public/<int:pk>/', views.ArticleDetailView.as_view(), name = 'article_detail'),
    path('structure/authors/', views.AuthorsListView.as_view(), name = 'authors_list'),
    path('structure/authors/<slug:slug>/', views.AuthorDetailView.as_view(), name = "author_detail"),
    path('search/', views.SearchResultViewSimple.as_view(), name = "search")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)