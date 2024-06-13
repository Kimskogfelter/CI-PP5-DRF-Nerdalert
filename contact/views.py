from rest_framework import generics, permissions, viewsets
from .models import ContactModel
from .serializers import ContactSerializer

class ContactListView(generics.ListCreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    

class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]
