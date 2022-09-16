from locale import currency
from django.db.models import Q
from pyexpat import model
from unicodedata import category
from django.conf import settings
from django.http import HttpResponse

from django.shortcuts import render

from django.views.generic import TemplateView,ListView,DetailView


from store.models import Category, Product
from store.models import Product

# Create your views here.

class WelcomePageView(TemplateView):
    template_name = 'Welcome.html'

class HomePageView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stripe_key']= settings.STRIPE_TEST_PUBLISHABLE_KEY
        return context

def charge(request):
    if request.method == 'POST':
        return render(request, 'charge.html')

class SearchResultListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Product.objects.filter(
            Q(name__icontains=query) | Q(price__icontains=query)
        )   


class LaptopFilterView(ListView):
    model = Product
    def get_queryset(self):
        return super().get_queryset().filter(Category__Name = 'Laptops') 
    context_object_name  = 'product_list'
    template_name = 'laptop_filter.html'        

class SmartphoneFilterView(ListView):
    model = Product
    def get_queryset(self):
        return super().get_queryset().filter(Category__Name = 'Smartphones')
    context_object_name = 'product_list'
    template_name = 'smartphone_filter.html'

class TVFilterView(ListView):
    model = Product
    def get_queryset(self):
        return super().get_queryset().filter(Category__Name = 'TVs')
    context_object_name = 'product_list'
    template_name = 'TV_filter.html'            