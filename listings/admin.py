from django.contrib import admin
from .models import LandListing, UserProfile, Payment
# Register your models here.

class LandListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'user', 'date_created')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'address')
    
admin.site.register(LandListing)
admin.site.register(UserProfile)
admin.site.register(Payment)
