from django import forms
from django.core.exceptions import ValidationError

from apps.users.models import FileModel
from apps.users.tasks import get_name_file, load_data_file


class LoadFileForm(forms.ModelForm):
    class Meta:
        model = FileModel
        fields = ('excel_file', )

    def clean_excel_file(self):
        file = self.cleaned_data['excel_file']
        name, extension = file.name.split('.')
        if extension != 'xls':
            raise ValidationError('It is not a valide format')
        return file

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        get_name_file.delay(instance.id)
        load_data_file.delay(instance.excel_file.path)
        return instance
