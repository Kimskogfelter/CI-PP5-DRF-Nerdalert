from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.ContactListView.as_view()),
    path('contact/<int:pk>/', views.ContactDetailView.as_view())
]
