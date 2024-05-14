# from django.db import models
#
#
# class BlogPost(models.Model):
#     title = models.CharField(max_length=255, null=True, blank=True)
#     short_description = models.TextField(max_length=255, null=True, blank=True)
#     full_description = models.TextField(max_length=2500, null=True, blank=True)
#
#     likes = models.IntegerField(default=0)
#     reposts = models.IntegerField(default=0)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         ordering = '-created_at'
#         verbose_name = 'Blog Post'
#         verbose_name_plural = 'Blog'
#         indexes = [
#             models.Index(fields=["title", "short_description"]),
#         ]
#
#     def __str__(self):
#         return self.title
#
#
# class BlogPostPhotos(models.Model):
#     post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='blog_photos')
#     photo_description = models.CharField(max_length=255, null=True, blank=True)
#     photo = models.ImageField(upload_to='images/', null=True, blank=True)


