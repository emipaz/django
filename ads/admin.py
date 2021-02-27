from django.contrib import admin
from ads.models import Ad

class PicAdmin(admin.ModelAdmin):
    exclude = ('picture', 'content_type')


# Register your models here.
admin.site.register(Ad)