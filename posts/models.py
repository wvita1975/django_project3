from django.db import models

# Create your models here.
class Post(models.Model): # nueva clase a incluir
    text = models.TextField()

    def __str__(self):  # para cambiar el nombre de la entrada a la base de datos
        return self.text[:50]
