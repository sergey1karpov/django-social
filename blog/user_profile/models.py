from PIL import Image
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    mobile_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=20, null=True, blank=True)
    job_title = models.CharField(max_length=50, null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='images/user_avatars', default='', null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            img1 = Image.open(self.avatar.path)
            if img1.height > 1500 or img1.width > 1500:
                output_size = (500, 500)
                img1.thumbnail(output_size)
                img1.save(self.avatar.path)
