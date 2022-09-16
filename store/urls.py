from unicodedata import name
from django.conf import settings

from django.conf.urls.static import static

from django.urls import path

from .views import (WelcomePageView,
                    HomePageView,
                    ProductDetailView,
                    SearchResultListView,
                    charge,
                    LaptopFilterView,
                    SmartphoneFilterView,
                    TVFilterView)



urlpatterns = [
    path('', WelcomePageView.as_view(),name='Welcome'),
    path('FJStore',HomePageView.as_view(),name="home"),
    path('<int:pk>', ProductDetailView.as_view(),name='product_detail'),
    path('charge', charge, name='charge'),
    path('FJStore/search/',SearchResultListView.as_view(),name='search_results'),
    path('FJStore/Laptops',LaptopFilterView.as_view(),name = 'laptop_filter'),
    path('FJStore/Smartphones',SmartphoneFilterView.as_view(),name = 'smartphone_filter'),
    path('FJStore/TVs',TVFilterView.as_view(),name = 'TV_filter'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)