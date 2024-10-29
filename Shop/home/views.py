from django.shortcuts import render
from django.views import View
from products.models import Product

class HomeView(View):

    def get(self, request):

        products = Product.objects.filter(available=True)
        return render(request, 'home/home.html', {'products':products})

