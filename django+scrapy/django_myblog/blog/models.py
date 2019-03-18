from django.db import models
from mdeditor.fields import MDTextField

class ExampleModel(models.Model):
    name = models.CharField(max_length=30)
    content = MDTextField(null=True)

class CurUser(models.Model):
    user_id = models.CharField(max_length=30)
    user_pw = models.CharField(max_length=30)
    mark = models.IntegerField(default=1)

class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    author = models.CharField(max_length=32, default='Author')
    category = models.CharField(max_length=32, default='Others')
    content = MDTextField(null=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# CREATE TABLE blog_users(
#     NUM INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
#     User_id VARCHAR(10) NOT NULL UNIQUE,
#     User_pw VARCHAR(100) NOT NULL DEFAULT '123456'
#     );