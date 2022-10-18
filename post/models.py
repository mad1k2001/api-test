from django.db import models
from django.contrib.auth.models import User


def upload_post_image(instance, filename):
    return "post/{user}/{filename}".format(
        user=instance.user,
        filename=filename
    )


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_post_image, null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
