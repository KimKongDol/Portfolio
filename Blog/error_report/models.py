from django.db import models

# Create your models here.


class ErrorReport(models.Model):
    title = models.CharField(max_length=200)
    lang = models.CharField(max_length=100)
    error = models.TextField()
    sol = models.TextField()
    how = models.TextField()

    def __str__(self):  # 클래스가 불러지면 대표로 타이틀을 달게함
        return self.title

    # def summary(self):
    #     return self.lyrics[:40]
