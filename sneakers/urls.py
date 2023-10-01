from django.urls import include, path
from .views import CreateBrand, CreateProducts

urlpatterns = [
    path('create', CreateBrand.as_view()),
    path('create-sneaker', CreateProducts.as_view()),
]