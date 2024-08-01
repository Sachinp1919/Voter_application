from django.urls import path
from .views import voter_add, show_details, candidate_details, update_Details, delete_Details


urlpatterns = [
    path('add/', voter_add, name='add_url'),
    path('show/', show_details, name='show_url'),
    path('details/<int:pk>/', candidate_details, name='details_url'),
    path('update/<int:pk>/', update_Details, name='update_url'),
    path('delate/<int:pk>/', delete_Details, name='delete_url')
]