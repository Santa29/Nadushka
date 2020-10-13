from django.contrib import admin
from django.urls import path, include

from .views import HomePageView, AboutPageView, StructurePageView, ResourcePageView, HistoryPageView, ModelPageView, PublicPageView, ContactsPageView, PublicDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('about/', AboutPageView.as_view(), name = 'about'),
    path('structure/', StructurePageView.as_view(), name = 'structure'),
    path('resource/', ResourcePageView.as_view(), name = 'resource'),
    path('history/', HistoryPageView.as_view(), name = 'history'),
    path('model/', ModelPageView.as_view(), name = 'model'),
    path('public/', PublicPageView.as_view(), name = 'public'),
    path('contacts/', ContactsPageView.as_view(), name = 'contacts'),
    path('public/<int:pk>/detail/', PublicDetailView.as_view(), name = 'public_detail')
]