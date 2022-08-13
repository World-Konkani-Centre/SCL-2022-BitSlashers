from django.contrib import admin
from .models import Profile
from .models import Product
from .models import Contact_us
# Register your models here.

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Contact_us)