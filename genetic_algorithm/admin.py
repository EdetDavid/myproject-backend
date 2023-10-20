from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Individual)
class IndividualModel(admin.ModelAdmin):
    list_filter = ('id', 'genes')
    list_display = ('id', 'genes')


@admin.register(Contact)
class ContactModel(admin.ModelAdmin):
    list_filter = ('name', 'email')
    list_display = ('name', 'email')
