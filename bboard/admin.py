from django.contrib import admin

# Register your models here.
from .models import Bb
from .models import Rubric

class BbAdmin (admin.ModelAdmin):
    list_display =('title', 'content', 'price', 'pablished','rubric')
    list_display_links = ('title', 'content', 'price')
    search_fields = ('title', 'content', 'price')



admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)