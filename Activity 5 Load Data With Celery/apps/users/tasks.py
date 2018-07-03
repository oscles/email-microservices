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
    with pandas.read_excel(path_file) as pd_users:
        for key, value in pd_users.iterrows():
            user = dict(value)
            user.pop(0, None)
            User.objects.create(**user)
    pd_users.close()
    return f'it was inserted {pd_users.size} one thousand users'
