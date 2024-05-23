from django.urls import path
from .views import AddAuthor

urlpatterns = [
    path('add-author', AddAuthor.as_view() )
]