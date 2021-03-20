from django.contrib import admin

# Register your models here.
from authm.models import CustomUser


admin.site.register(CustomUser)

