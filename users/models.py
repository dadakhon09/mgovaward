from django.contrib.auth.models import AbstractUser
from django.db import models

USER_TYPE = (
    (0, 'Admin'),
    (1, 'Patient'),
    (2, 'Doctor'),
)


class UserProfile(AbstractUser):
    user_type = models.IntegerField(choices=USER_TYPE, null=True, blank=True)

    class Meta:
        db_table = 'user_profile'

    def __str__(self):
        return self.username
