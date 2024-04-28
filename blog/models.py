from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth import get_user_model # from django.contrib.auth.models import Userc1
from django.contrib.contenttypes.fields import GenericForeignKey , GenericRelation
from django.contrib.contenttypes.models import ContentType




class Tag(models.Model):
    value = models.TextField(max_length=100)
    
    def __str__(self):
        return  self.value



    
class Comment(models.Model):
    creater = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    content = models.TextField()
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = GenericForeignKey("content_type", "object_id") 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
    
    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True,db_index=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")
    comments = GenericRelation(Comment)

    def __str__(self):
        return self.title
    
    
class AuthorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name='profile')
    bio = models.TextField()
    
    def __str__(self):
        return f'{self.__class__.__name__} objectfor {self.user}'