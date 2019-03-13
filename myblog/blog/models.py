from django.db import models


class Users(models.Model):
    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=30)
    # user_ticket = models.CharField(max_length=30, null=True)
    

class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')
    author = models.CharField(max_length=32, default='Author')
    category = models.CharField(max_length=32, default='Others')
    content = models.TextField(null=True)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# CREATE TABLE blog_users(
#     NUM INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
#     User_id VARCHAR(10) NOT NULL UNIQUE,
#     User_pw VARCHAR(100) NOT NULL DEFAULT '123456'
#     );