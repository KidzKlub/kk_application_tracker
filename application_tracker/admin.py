from django.contrib import admin

from .models import *


class ReferenceAdmin(admin.TabularInline):
    model = Reference

class ASMAdmin(admin.ModelAdmin):
    inlines = [ReferenceAdmin]

admin.site.register(ApplicationStateModel, ASMAdmin)
admin.site.register(ApplicationForm)
admin.site.register(Reference)

