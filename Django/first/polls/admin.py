from django.contrib import admin

from .models import Question,Choice

admin.register(Question,Choice)(admin.ModelAdmin)