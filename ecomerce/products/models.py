from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to="productImages")
    created = models.DateTimeField('auto_now_add=True')
    active = models.BooleanField()
# Create your models here.
