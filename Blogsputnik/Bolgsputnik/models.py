from django.db import models
# Create your models here.
class Posts(models.Model):
    titulo = models.CharField(max_length=20, null=False, blank=False)
    texto = models.TextField()
    autor = models.CharField(max_length=100, null=False, blank=False)
    data_plublic = models.DateTimeField(auto_now_add = True)


