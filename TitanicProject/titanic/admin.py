from django.contrib import admin
from titanic.models import MLModel

# Register your models here.


@admin.register(MLModel)
class MLModelAdmin(admin.ModelAdmin):
    list_display = ['id','model']
