from django.contrib import admin
from massadv.models import StItems
from massadv.models import StImages
from massadv.models import StCat
from massadv.models import StCategories
from massadv.models import StUsers
from massadv.forms import StUsersForm

class StItemsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'consignor__username']
    

class StUsersAdmin(admin.ModelAdmin):
    search_fields = ['username', 'firstname', 'lastname']
    form = StUsersForm

admin.site.register(StItems, StItemsAdmin)
admin.site.register(StImages)
admin.site.register(StCat)
admin.site.register(StCategories)
admin.site.register(StUsers, StUsersAdmin)
# Register your models here.
