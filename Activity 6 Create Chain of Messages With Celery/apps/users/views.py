# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from apps.users.forms import LoadFileForm


class LoadFileCreateView(CreateView):
    template_name = 'create_file.html'
    success_url = '.'
    form_class = LoadFileForm
