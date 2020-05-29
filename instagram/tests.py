from django.test import TestCase
from .models import Image,Comments

# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.image=Image(image_name='Test Image',image_caption='Test image caption')
        self.image.save()
        
    #TEST FOR SAVE
    def test_save(self):
        self.image.save_image()
        save=Image.objects.filter(image_name=self.image.image_name)
        self.assertTrue(len(save)==1)
        
    def test_delete_image(self):
        Image.delete_image(self.image.pk)
        deleted=Image.objects.all()
        self.assertTrue(len(deleted)==0)