from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Sex:
        MALE = 'male'
        FEMALE = 'female'

        CHOICES = (
            (MALE, 'Мужчина'),
            (FEMALE, 'Женщина'),
        )

    phone = models.CharField(
        'телефон',
        blank=True,
        max_length=14,
    )
    sex = models.CharField(
        'пол',
        max_length=6,
        choices=Sex.CHOICES,
        default=Sex.FEMALE,
    )
    is_teacher = models.BooleanField(
        'хочу создавать курсы',
        default=False,
    )



class Node(models.Model):
    class TypeList:
        DEPARTMENT = 'department'
        TEAM = 'team'
        POSITION = 'position'

        CHOICES = (
            (DEPARTMENT, 'Department'),
            (TEAM, 'Team'),
            (POSITION, 'Position'),
        )

    title = models.CharField(
        'title',
        max_length=50
    )
    types = models.CharField(
        choices=TypeList.CHOICES,
        max_length=50,
    )

    def get_users(self):
        return self.department_node.all()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return 'ссылка'


class UserPosition(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Node, related_name='team_node', on_delete=models.PROTECT)
    position = models.ForeignKey(Node, related_name='position_node', on_delete=models.PROTECT)
    department = models.ForeignKey(Node, related_name='department_node', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
