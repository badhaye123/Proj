from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import Approver, Requester, User,ApprovalRequest


class ApproverSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    age = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.is_approver = True
        user.save()
        approver = Approver.objects.create(user=user)
        return approver


class RequesterSignUpForm(UserCreationForm):
    name = forms.CharField(required=True)
    age = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.is_requester = True
        user.save()
        requester = Requester.objects.create(user=user)

        requester.save()

        return requester



class ApprovalRequestForm(forms.ModelForm):
    class Meta:
        model = ApprovalRequest
        fields = ['type','assigned_to','date_of_deployment','commit_id',
                  'branch','deployed_environment','changes',]