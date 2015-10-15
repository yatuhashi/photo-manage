from django.contrib import admin
from scsho.models import anime,sc_data

# Register your models here.
class animeAdmin(admin.ModelAdmin):
     list_display = ('id', 'ani_ti','admin_image_view','created',)
     ordering = ('-created',)
     pass


admin.site.register(anime)
admin.site.register(sc_data,animeAdmin)
