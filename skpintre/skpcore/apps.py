from django.apps import AppConfig

# sets the app to use the skpcore as the the new config
class SkpcoreConfig(AppConfig):
    name = 'skpcore'

    # adds the signals to be used when posting
    def ready(self):
    	import skpcore.signals