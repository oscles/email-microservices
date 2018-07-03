from __future__ import absolute_import, unicode_literals

import pandas
from django.contrib.auth.models import User

from apps.users.models import FileModel
from load_data_excel_celery.celery import app


@app.task
def get_name_file(pk_file):
    instance = FileModel.objects.get(pk=pk_file)
    return instance.get_name


@app.task
def load_data_file(path_file):
    pd_users = pandas.read_excel(path_file)
    for key, value in pd_users.iterrows():
        data_user = dict(value)
        data_user.pop(0, None)
        User.objects.create(**data_user)
    return f'it was inserted {pd_users.size} one thousand pd_users'
