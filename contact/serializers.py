from rest_framework import serializers
from .models import ContactModel

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel

        fields = ['contact_name', 'contact_topic', 'contact_email', 'contact_message', 'created_at']