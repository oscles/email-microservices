# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class FileModel(models.Model):
    excel_file = models.FileField(upload_to='files_excel')

    @property
    def get_name(self):
        dirname, name_file = self.excel_file.name.split('/')
        return name_file

    def __str__(self):
        return self.get_name
