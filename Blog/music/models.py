from django.db import models

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, null='True')
    singer = models.CharField(max_length=100)
    lyrics = models.TextField()

    def __str__(self):  # 클래스가 불러지면 대표로 타이틀을 달게함
        return self.title

    def summary(self):
        return self.lyrics[:40]
