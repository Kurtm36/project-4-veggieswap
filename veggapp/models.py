from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

STATUS = ((0, "Draft"), (1, "Published"))

# Post Model

class Post(models.Model):
    # Basic Post information
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(max_length=200)
    excerpt = models.TextField(blank=True)

    # Author of the Post
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_posts"
    )

    # Summary field
    summary = models.CharField(max_length=500, blank=True)

    # Status Field
    status = models.IntegerField(choices=STATUS, default=0)

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    # Save
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
            
    def __str__(self):
        return self.title
