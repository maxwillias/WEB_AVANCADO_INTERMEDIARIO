from django.urls import path
from .views import index
from .views import index, produto

urlpatterns = [
    path('', index, name='index'),
    path('produto/<int:id>', produto, name='produto'),
]