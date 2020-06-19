from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Bruger

def bruger_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='Bruger')
		instance.groups.add(group)
		Bruger.objects.create(
			user=instance,
			name=instance.username,
			)
		#print('Profile created!')

post_save.connect(bruger_profile, sender=User)