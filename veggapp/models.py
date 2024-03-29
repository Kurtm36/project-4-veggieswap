from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

CATAGORY = ((0, "Fruit"), (1, "Vegatable"), (2, "Plant"))

## POST MODEL

class UserPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=0)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
    featured_image = CloudinaryField("image", default="placeholder")
    placeholder_image = models.CharField(max_length=300, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(max_length=2000, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    catagory = models.IntegerField(choices=CATAGORY, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

## COMMENT MODEL

class UserComments(models.Model):
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"