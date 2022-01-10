from django.db import models

# Create your models here.


class ErrorReport(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    lang = models.CharField(max_length=100)
    error = models.TextField()
    sol = models.TextField()
    how = models.TextField(blank=True, null=True)
    # uploade_to는 어디어디에 저장하겠다는 의미이다. 고로 따로 파일에 이 내용이 저장될 것이다.
    image = models.ImageField(upload_to="image/", blank=True, null=True)

    def __str__(self):  # 클래스가 불러지면 대표로 타이틀을 달게함
        return self.title

    # def summary(self):
    #     return self.lyrics[:40]
