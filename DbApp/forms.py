from django import forms
import datetime


class GetDataForm(forms.Form):
    date = forms.DateField(label='Дата', initial=datetime.date.today().strftime('%d-%m-%Y'), input_formats=['%d-%m-%Y'])
    user_name = forms.CharField(label='Водитель', empty_value=None, required=False)
    vehicle_plate = forms.CharField(label='Автобус', empty_value=None, required=False)
