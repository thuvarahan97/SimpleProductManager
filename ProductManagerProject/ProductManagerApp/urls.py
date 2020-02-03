from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='home_page'),
    path('add_product', views.product_form, name='add_product'),
    path('delete/<str:id>/', views.product_delete, name='product_delete'),
    path('results', views.search_product, name='search_product'),
]