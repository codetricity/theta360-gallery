from django.contrib import admin
from suit.admin import SortableModelAdmin
from .models import Job, Viewer

class JobAdmin(SortableModelAdmin):
    sortable = 'order'

admin.site.register(Job, JobAdmin)
admin.site.register(Viewer)
