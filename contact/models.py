from django.db import models


class ContactModel(models.Model):
    """
    Model to create the messages from the contact form.
    The model also has a response field for the admins when
    they are logged in on the admin page. The admin can then
    answer on the messages sent from the users.
    """
    contact_name = models.CharField(max_length=150)
    contact_topic = models.CharField(max_length=300)
    contact_email = models.EmailField()
    contact_message = models.TextField(max_length=750)
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    admin_answer = models.TextField(blank=True, null=True)
    
    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self):
        return f"Contact message from {self.contact_name} : {self.contact_topic}"