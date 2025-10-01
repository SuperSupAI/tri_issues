from datetime import date
from django import forms
from .models import ISSUE

class OpenISSUE(forms.ModelForm):
    status = 'OPEN'
    class Meta:
        model = ISSUE
        fields = '__all__'
        exclude = ['executor', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'value': date.today(),'format': '%d/%m/%Y','type':'date', 'min':date.today()}),
        }

class UpdateISSUE(forms.ModelForm):
    status = forms.ChoiceField (choices=[('on going' , 'ON GOING'),('closed' , 'CLOSED')])
    class Meta:
        model = ISSUE
        fields = ['progress','status','date','priority']
        widgets = {
            'date': forms.DateInput(attrs={'value': date.today(),'format': '%d/%m/%Y','type':'date', 'min':date.today()}),
       }

class EditISSUE(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['issue'].disabled = True
        self.fields['problem'].disabled = True

    class Meta:
        model = ISSUE
        fields = '__all__'
        exclude = ['executor','machine','model','serial_no', 'customer']
        widgets = {
            'date': forms.DateInput(attrs={'value': date.today(),'format': '%d/%m/%Y','type':'date'}),
        }