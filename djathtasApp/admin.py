from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Video)


class AnetarsimiAdmin(admin.ModelAdmin):
    list_display = ('emer', 'mbiemer', 'email', 'datelindja', 'gjinia')
    list_display_links = ('emer', 'mbiemer', 'email', 'datelindja', 'gjinia')
    search_fields = ('emer', 'mbiemer', 'email')
    list_filter = ('gjinia', 'qarku', 'bashkia')
admin.site.register(Anetarsimi,AnetarsimiAdmin)
admin.site.register(ArtikujInfomues)
admin.site.register(ArtikujImage)
admin.site.register(ArtikujVideo)
