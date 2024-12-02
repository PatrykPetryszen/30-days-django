from django.contrib import admin
from .models import CustomUser #. means "current package/directory"

admin.site.register(CustomUser)
# Register your models here.
