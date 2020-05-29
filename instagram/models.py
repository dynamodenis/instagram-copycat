from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to='images/', blank=True,default='default.jpg')
    image_name=models.CharField(max_length=30)
    image_caption=models.TextField()
    likes=models.ImageField(default=0)
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
              
    def __str__(self):
        return self.image_name
    
class Comments(models.Model):
    image=models.ForeignKey(Image, on_delete=models.CASCADE)
    comment=models.TextField()
    likes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.comment
    