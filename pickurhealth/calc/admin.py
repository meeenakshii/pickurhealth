from django.contrib import admin
from .models import Recipe
from .models import *

admin.site.register(Type)
admin.site.register(Recipe)

