from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Husreglerform)
admin.site.register(Bruger)
admin.site.register(Senestenyt)
admin.site.register(Blogpost)
admin.site.register(Blogcomment)
admin.site.register(Infoform)