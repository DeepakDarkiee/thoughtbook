from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.text import slugify
from ckeditor_uploader.fields import  RichTextUploadingField
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)
            
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    Content = models.TextField(null=True)
    phone= models.CharField(max_length=13,null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return "Contact {} by {}".format(self.body, self.name)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    created_by=models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    # manually deactivate inappropriate comments from admin site
    reply = models.ForeignKey('self', null=True, blank=True, related_name='replies',on_delete=models.CASCADE)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created_on',)

    def __str__(self):
        return "Comment {} by {}".format(self.content, self.created_by)

