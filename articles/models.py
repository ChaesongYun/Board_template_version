from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    # 작성자를 외래키로 설정
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    # fields
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    # 어떤 글에 댓글을 작성할지? -> 글을 외래키로 설정
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    # 작성자를 외래키로 설정
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # fields
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

