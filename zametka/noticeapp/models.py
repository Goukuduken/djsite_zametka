from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    #photo = models.ImageField(upload_to="photos/%Y/%m/%d)

    def __str__(self):
        return self.title

    class Meta: #for admin board
        ordering = ['time_create', 'title']



