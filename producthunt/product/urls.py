from django.urls import path
from .views import *

urlpatterns = [
    path('create/', create, name='create'),
    path('list/', list, name='list'),
    path('<int:product_id>', detail, name='detail'),
    path('<int:product_id>/edit', edit, name='edit'),
    path('<int:product_id>/delete', delete, name='delete'),
    path('<int:product_id>/upvote', upvote, name='upvote'),
]