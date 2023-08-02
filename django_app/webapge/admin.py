from django.contrib import admin

# Register your models here.
from .models import Student 

admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('std_id','prefix', 'name', 'lastname', 'phone')
    search_fields = ('name', 'lastname')
    