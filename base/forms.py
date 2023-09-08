from django.forms import ModelForm
from .models import business


class businessForm(ModelForm):
    class Meta:
        model = business
        fields = "__all__"
