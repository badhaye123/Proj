from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.

class User(AbstractUser):
    is_approver = models.BooleanField(default=False)
    is_requester = models.BooleanField(default=False)


class Approver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f'{self.user}'


class Requester(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f'{self.user}'


class ApprovalRequest(models.Model):
    type_choice = (('deployment', 'deployment'),)
    deployment_env_choices = (('development', 'development'),
                              ('UAT', 'UAT'),
                              ('production', 'production'))
    type = models.CharField(max_length=64, choices=type_choice)
    assigned_to = models.ForeignKey(Approver, on_delete=models.CASCADE)
    requester = models.ForeignKey(Requester, on_delete=models.CASCADE)
    date_of_deployment = models.DateField()
    commit_id = models.CharField(max_length=255)
    branch = models.CharField(max_length=64)
    deployed_environment = models.CharField(max_length=64, choices=deployment_env_choices)
    changes = models.TextField()
    status = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
