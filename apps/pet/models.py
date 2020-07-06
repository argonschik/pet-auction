from django.db import models
from django.contrib.auth import get_user_model

from utils.framework.models import SystemBaseModel

User = get_user_model()


class Pet(SystemBaseModel):
    """
    Model of Pet entity
    """

    breed = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    owner = models.ForeignKey(
        to=User,
        related_name='owner_of_pets',
        on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nickname}: {self.breed}: {self.owner}"

