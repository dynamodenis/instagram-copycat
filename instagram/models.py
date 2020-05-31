from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=30, blank=True)
    image_caption=models.TextField()
    likes=models.ManyToManyField(User,related_name='image_likes', blank=True)
    posted=models.DateTimeField(auto_now_add=True)
    
    def save_image(self):
        self.save()
    @classmethod   
    def delete_image(cls,delete_id):
        Image.objects.filter(pk=delete_id).delete()
        
    @classmethod
    def update_caption(cls,image_id,caption):
        Image.objects.filter(pk=image_id).update(image_caption=caption)
        updated=Image.objects.get(pk=image_id)
        return updated
    @classmethod
    def get_comments(cls,image_id):
        image=Image.objects.get(pk=image_id)
        image_comments=image.comments_set.all()
        return image_comments
              
    def __str__(self):
        return self.image_caption
    
class Comments(models.Model):
    image=models.ForeignKey(Image, on_delete=models.CASCADE)
    comment=models.TextField()
    likes=models.ManyToManyField(User,related_name='comment_likes', blank=True)
    
    def __str__(self):
        return self.comment
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='profile/',default='default.png')
    bio=models.CharField(max_length=100,blank=True)
    
    def __str__(self):
        return self.user.username