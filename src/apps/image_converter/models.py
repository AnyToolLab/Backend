from django.db import models

class File(models.Model):
    file = models.FileField(upload_to='image_converter/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file.name} (Created on {self.created_at})"