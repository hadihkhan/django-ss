from django.contrib import admin
from .models import Students
# Register your models here.



class StudentAdmins(admin.ModelAdmin):
    empty_value_display = '-empty-'
    labels = {
        'name': 'Category Name',
    }
admin.site.register(Students, StudentAdmins)

