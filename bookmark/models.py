from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('TITLE', max_length=100, blank=True)   # 공백을 가질 수 있다.
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return f"{self.title} and {self.url}"
