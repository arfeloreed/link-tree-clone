from django.db import models


# Create your models here.
class Profile(models.Model):
    BG_CHOICES = (
        ("blue", "Blue"),
        ("grey", "Grey"),
        ("green", "Green"),
    )

    name = models.CharField(max_length=120)
    slug = models.SlugField()
    bg_color = models.CharField(max_length=120, choices=BG_CHOICES)

    def __str__(self):
        return self.name


# model for links
class Link(models.Model):
    name = models.CharField(max_length=120)
    url = models.URLField()
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return self.name
