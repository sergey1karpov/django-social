from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, FileExtensionValidator


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    phone_number = models.CharField(max_length=20, blank=True, default='', unique=True, validators=[MaxLengthValidator(20), MinLengthValidator(5)])
    mobile_number = models.CharField(max_length=20, blank=True, default='', unique=True,validators=[MaxLengthValidator(20), MinLengthValidator(5)])
    city = models.CharField(max_length=20, blank=True, default='', validators=[MaxLengthValidator(20), MinLengthValidator(5)])
    country = models.CharField(max_length=20, blank=True, default='', validators=[MaxLengthValidator(20), MinLengthValidator(5)])
    job_title = models.CharField(max_length=50, blank=True, default='', validators=[MaxLengthValidator(50), MinLengthValidator(5)])
    company = models.CharField(max_length=50, blank=True, default='', validators=[MaxLengthValidator(50), MinLengthValidator(5)])
    avatar = models.ImageField(upload_to='images/user_avatars', default='', validators=[FileExtensionValidator(['jpeg', 'jpg', 'png'])])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            img1 = Image.open(self.avatar.path)
            if img1.height > 1500 or img1.width > 1500:
                output_size = (500, 500)
                img1.thumbnail(output_size)
                img1.save(self.avatar.path)
