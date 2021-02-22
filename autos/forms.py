######  form.py ###################
from autos.models import Auto , Make
from django.forms import ModelForm

class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'
###################################