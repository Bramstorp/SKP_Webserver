from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Bruger

# this signal function is called when a user signups on the site 
def bruger_profile(sender, instance, created, **kwargs):
	if created:
		# if the user gets created the user will be added to a "Bruger" group 
		group = Group.objects.get(name='Bruger')
		instance.groups.add(group)
		# this creates a Bruger for the user so we can use user group permisions
		Bruger.objects.create(
			user=instance,
			name=instance.username,
			)
		#print('Profile created!')

# saves the bruger / User and add it to the database
post_save.connect(bruger_profile, sender=User)