from django.contrib import admin
from .models import Tag, Priority

admin.site.site_header = 'Pro Tasks'
admin.site.site_title =  'Pro Tasks'
admin.site.index_title = 'Panel de administración'

admin.site.register(Tag)
admin.site.register(Priority)