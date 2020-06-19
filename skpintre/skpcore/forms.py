from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

class HusreglForm(ModelForm):
	class Meta:
		model = Husreglerform
		fields = "__all__"

class Submitcomment(forms.Form):
	comment = forms.CharField(widget=forms.Textarea(attrs={
		"class": "form-control",
		"placeholder": "Comment",
		"rows": "3"
	}))