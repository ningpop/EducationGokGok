from django.db import models

# Create your models here.
''' 
*멘토 클래스*
- 회원 기본 정보(Info)클래스 상속 
- 사진(Image)
- 분야(Major)
- 지역(Area)
- 소개 글(description)
- 카톡 오픈 채팅 주소(Contact)
'''
class Mento(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=225)
    major = models.CharField(max_length=10)
    area = models.CharField(max_length=10)
    body = models.TextField()
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.title