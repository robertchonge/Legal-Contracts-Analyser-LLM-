from django.db import models

class UploadedContract(models.Model):
    file = models.FileField(upload_to='contracts/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

