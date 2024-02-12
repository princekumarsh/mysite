from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    desc = models.TextField()
    date = models.DateTimeField( auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name 