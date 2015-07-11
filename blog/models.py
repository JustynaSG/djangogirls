from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User') #odwołanie do innego obiektu
    title = models.CharField(max_length=200) #max 200 znaków
    text = models.TextField() #brak ograniczenia długości
    created_date = models.DateTimeField(        #data utworzenia posta na blogu, 
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):              #self=jednen post
        self.published_date = timezone.now()
        self.save()     #zapis do bd

    def __str__(self):
        return self.title       #tytuły