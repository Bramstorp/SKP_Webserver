from django.apps import AppConfig

class SkpcoreConfig(AppConfig):
    name = 'skpcore'

    def ready(self):
    	import skpcore.signals