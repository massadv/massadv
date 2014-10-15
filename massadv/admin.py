from django.contrib import admin
from massadv.models import Items, Claim
from massadv.models import Images
from massadv.models import Cat
from massadv.models import Categories
from massadv.models import Users
from massadv.forms import UsersForm

class StItemsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description', 'consignor__username']
    

class StUsersAdmin(admin.ModelAdmin):
    search_fields = ['username', 'firstname', 'lastname']
    form = UsersForm

admin.site.register(Items, StItemsAdmin)
admin.site.register(Images)
admin.site.register(Cat)
admin.site.register(Categories)
admin.site.register(Users, StUsersAdmin)
admin.site.register(Claim)

# Register your models here.
