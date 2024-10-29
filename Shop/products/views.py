from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404

from products.models import Product


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'products/product_detail.html', {'product':product})

