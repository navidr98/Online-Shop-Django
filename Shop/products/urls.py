from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]