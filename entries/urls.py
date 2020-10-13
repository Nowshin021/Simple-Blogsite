from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry-detail'),
    path('create_entry/', CreateEntryView.as_view(success_url="/"), name='create-entry'),
    path('edit_entry/<int:pk>/', EditEntryView.as_view(success_url="/"), name='edit-entry'),
    path('delete_entry/<int:pk>/', DeleteEntryView.as_view(success_url="/"), name='delete-entry'),
]