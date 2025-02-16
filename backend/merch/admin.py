from django.contrib import admin
from . import models



class MerchAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Merch, MerchAdmin)

class MerchImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.MerchImage, MerchImageAdmin)