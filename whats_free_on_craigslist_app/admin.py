from django.contrib import admin
from .models import Search
from .models import Listing

# Register your models here.
admin.site.register(Search)
admin.site.register(Listing)
