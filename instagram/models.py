from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Images(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    image_name=models.CharField(max_length=30, blank=True)
    image_caption=models.TextField()
    likes=models.ManyToManyField(User,related_name='image_likes', blank=True)
    posted=models.DateTimeField(auto_now_add=True)
    
    def save(self):
        super().save()
        
        img=Image.open(self.image.path)
        
        if img.height>720 and img.width>720:
            size=(720,720)
            img.thumbnail(size)
            img.save(self.image.path)
    
    def save_image(self):
        self.save()
    @classmethod   
    def delete_image(cls,delete_id):
        Images.objects.filter(pk=delete_id).delete()
        
    @classmethod
    def update_caption(cls,image_id,caption):
        Images.objects.filter(pk=image_id).update(image_caption=caption)
        updated=Images.objects.get(pk=image_id)
        return updated
    @classmethod
    def get_comments(cls,image_id):
        image=Images.objects.get(pk=image_id)
        image_comments=image.comments_set.all()
        return image_comments
              
    def __str__(self):
        return self.image_caption
    
class Comments(models.Model):
    image=models.ForeignKey(Images, on_delete=models.CASCADE)
    comment=models.CharField(max_length=500)
    likes=models.ManyToManyField(User,related_name='comment_likes', blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comment
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    picture=models.ImageField(upload_to='profile/',default='default.png')
    bio=models.CharField(max_length=100,blank=True)
    followers=models.ManyToManyField(User,blank=True,related_name='followers')
    following=models.ManyToManyField(User,blank=True,related_name='following')
    
    def __str__(self):
        return self.user.username
    
    def save(self):
        super().save()
        img=Image.open(self.picture.path)
        
        if img.height >300 and img.width>300:
            size=(300,300)
            img.thumbnail(size)
            img.save(self.picture.path)