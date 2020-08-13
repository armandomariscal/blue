from django.contrib.auth.models import User
from django.db import models


class CommonModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Movie(CommonModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to="static/movies/")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
