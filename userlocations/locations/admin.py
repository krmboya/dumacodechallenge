from django.contrib import admin

import models

class CountyAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.County, CountyAdmin)

class WardAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Ward, WardAdmin)


class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Location, LocationAdmin)
