from django.contrib import admin
from .models import Role, Task, Achievement

# Register your models here.
admin.site.register(Role)
admin.site.register(Task)
admin.site.register(Achievement)