from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='customuser',
        blank=True,
        help_text='Specific permissions for this user.',
    )

class Anime(models.Model):
    code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=150)
    image = models.ImageField(upload_to='anime_images/', null=True, blank=True)
    status = models.CharField(max_length=50)
    comment = models.CharField(max_length=150)

    class Meta:
        app_label = 'animeapp'

        def __str__(self):
            return self.name