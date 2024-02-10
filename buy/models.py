from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1,"Listed"))

# Create your models here.

class Listing(models.Model):
    """
    Store a single buy listing entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    image_1 = CloudinaryField('image_1', default='placeholder')
    image_2 = CloudinaryField('image_2', default='placeholder')
    image_3 = CloudinaryField('image_3', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    bid_timer = models.DurationField()
    price = price = models.DecimalField(max_digits=10, decimal_places=2)
    current_bid = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    reserve = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ("created_on")

    def __str__(self):
        return f"The title of this post is {self.title} | written by {self.author}"