from django.db import models


class Contact(models.Model):
    """
    A class model for contact page
    """
    name = models.CharField(max_length=254, null=False, blank=False)
    contact_email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return str(self.name)
