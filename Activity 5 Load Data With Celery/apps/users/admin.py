# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from apps.users.models import FileModel


@admin.register(FileModel)
class FileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_name', )
    ordering = ('pk', )