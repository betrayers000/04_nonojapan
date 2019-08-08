from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    name_en = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    nation = models.CharField(max_length=50)
    replace = models.CharField(max_length=50)
    
    def replace_list(self):
        return self.replace.split(',')



class Comment(models.Model):
    content = models.CharField(max_length=150)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)