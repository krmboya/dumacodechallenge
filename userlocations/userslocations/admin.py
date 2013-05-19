from django.contrib import admin

import models

class MappingAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Mapping, MappingAdmin)
