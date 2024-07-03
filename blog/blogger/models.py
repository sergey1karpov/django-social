from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, FileExtensionValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True)
    title = models.CharField(validators=[MaxLengthValidator(20), MinLengthValidator(5)])
    short_description = models.TextField(blank=True, default='', validators=[MaxLengthValidator(150)])
    full_description = models.TextField(blank=True, default='', validators=[MaxLengthValidator(2500)])
    likes = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='images/posts/', blank=True, validators=[FileExtensionValidator(['jpeg', 'jpg', 'png'])])

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog'
        indexes = [
            models.Index(fields=["title", "short_description"]),
        ]

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.photo and self.photo.size > 4194304:
            raise ValidationError("Photo size must be less than 4MB")



