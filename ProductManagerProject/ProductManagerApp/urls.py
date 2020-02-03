from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_home, name='home-page'),
    path('add_product', views.product_form, name='add-product'),
    path('delete/<str:id>/', views.product_delete, name='product_delete'),
]