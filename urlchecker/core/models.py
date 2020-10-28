from django.db import models


class Url(models.Model):
    body = models.TextField()
