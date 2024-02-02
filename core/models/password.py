from django.db import models
from autoslug import AutoSlugField


class Password(models.Model):
    title = models.CharField(max_length=50)
    password = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    slug = AutoSlugField(populate_from='title', unique=True)

    class Meta:
        db_table = 'password'
        verbose_name = 'Password'
        verbose_name_plural = 'Passwords'

    def __str__(self):
        return self.title