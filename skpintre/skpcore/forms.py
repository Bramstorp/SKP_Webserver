from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

# this is the user form import from the premade UserCreationModel Form
# we set the model as the build in user model and the fiields for creating a user
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

# creates a form for the HusRegler Model and getting all fields from it 
class HusreglForm(ModelForm):
	class Meta:
		model = Husreglerform
		fields = "__all__"

# custome form used for comment part in the ide template
class Submitcomment(forms.Form):
	comment = forms.CharField(widget=forms.Textarea(attrs={
		"class": "form-control",
		"placeholder": "Comment",
		"rows": "3"
	}))