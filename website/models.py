from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    school_name = models.CharField(max_length=255, default="")
    phone = models.CharField(max_length=255, default="")
    email = models.EmailField()
    message = models.TextField()
    file_url = models.CharField(max_length=1024, default="")

    def __str__(self):
        return self.name


class Document(models.Model):
    file_name =  models.CharField(max_length=255, default="")
    file = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
