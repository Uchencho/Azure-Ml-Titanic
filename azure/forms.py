from django import forms
from .models import Predict

class PredictForm(forms.ModelForm):
    class Meta:
        model = Predict
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(PredictForm, self).__init__(*args, **kwargs)
