from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(default=timezone.now)
    phone = models.IntegerField(default=0)
    image = models.ImageField(default="default_img.png", upload_to='profile_img')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Profiles"

    def save(self, *args, **kwargs):  # overriding the save method of the model
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            resized_img = (200, 300)
            img.thumbnail(resized_img)
            img.save(self.image.path)
