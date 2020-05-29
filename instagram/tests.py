from django.test import TestCase
from .models import Image,Comments

# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.image=Image(image_name='Test Image',image_caption='Test image caption')
        self.image.save()
        self.comment=Comments(image=self.image,comment="test comment")
        self.comment.save()
    #TEST FOR SAVE
    def test_save(self):
        self.image.save_image()
        save=Image.objects.filter(image_name=self.image.image_name)
        self.assertTrue(len(save)==1)
        
    def test_delete_image(self):
        Image.delete_image(self.image.pk)
        deleted=Image.objects.all()
        self.assertTrue(len(deleted)==0)
        
    def test_update_caption(self):
        updated=Image.update_caption(self.image.pk,"Test image has been updated")
        self.assertTrue(updated.image_caption,"Test image has been updated")
        
    def test_get_comments(self):
        comments=Image.get_comments(self.image.pk)
        self.assertTrue(len(comments)==1)