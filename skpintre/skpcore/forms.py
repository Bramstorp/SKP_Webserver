from .models import *
from django.forms import ModelForm


class HusreglForm(ModelForm):
	class Meta:
		model = Husreglerform
		fields = "__all__"