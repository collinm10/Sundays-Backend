from django.contrib import admin
from . models import User, AssignmentType, Class, Assignment

# Register your models here.
class SundaysAdmin(admin.ModelAdmin):
    myModels = [Class, Assignment, User, AssignmentType]
    admin.site.register(myModels)