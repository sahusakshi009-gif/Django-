from django.contrib import admin
from .models import Employee
admin.site.register(Employee)
class Noteadmin(admin.ModelAdmin):
    list_display=('name', 'email', 'phone', 'department', 'salary', 'joining_date')
# Register your models here.
