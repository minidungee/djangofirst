from django.db import models

# Create your models here.
#apiapp_soccer이라는 테이블을 생성
class Soccer(models.Model):
  bid = models.IntegerField(primary_key=True)
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  publisheddate = models.DateField()