from django import forms
from .widgets import CustomClearableFileInput
from .models import Ebook, Category, Ebook_reader


class EbookForm(forms.ModelForm):

    class Meta:
        model = Ebook
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)  # noqa: disable=line-too-long

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.exclude(name__in=['kindle', 'kobo'])
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class EbookForms(forms.ModelForm):

    class Meta:
        model = Ebook_reader
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)  # noqa: disable=line-too-long

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.filter(name__in=['kindle', 'kobo'])
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
