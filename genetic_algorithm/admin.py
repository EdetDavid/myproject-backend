from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Individual)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('id', 'genes')
    list_display = ('id', 'genes')




admin.site.register(OptimizationResult)
