

from email.policy import default
from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from .models import *
from django.forms import CheckboxInput, DateInput, ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput
from django.conf import settings


class AccountForm(ModelForm):
    CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = forms.CharField(
        label='gender', widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = Account
        fields = '__all__'
        exclude = ('user',)

class EmailForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude = ()
  


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        exclude = ()


class ScheduleForm(ModelForm):
    date = forms.DateField(label='date', widget=forms.DateInput(
        format='%m/%d/%Y'), input_formats=settings.DATE_INPUT_FORMATS)
    everyYear = forms.CharField(
        label='everyYear', widget=forms.CheckboxInput(attrs={'checked': True, 'None': False}))

    class Meta:
        model = Schedule
        fields = '__all__'
        exclude = ('user', 'date')
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
            'dm': CheckboxInput(),

        }


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        exclude = ('user', 'date_created')


class CaseForm(ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        exclude = ('user', 'date_created')


class RxForm(ModelForm):
    class Meta:
        model = Rx
        fields = '__all__'
        exclude = ()


class HistoryForm(ModelForm):
    CHOICES = [('Right', 'Right'), ('Left', 'Left')]
    dominant_hand = forms.CharField(
        label='dominant_hand', widget=forms.RadioSelect(choices=CHOICES))

    dominant_eye = forms.CharField(
        label='dominant_eye', widget=forms.RadioSelect(choices=CHOICES))

    class Meta:
        model = History
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'dm': CheckboxInput(),
            'hpn': CheckboxInput(),
            'allergies': CheckboxInput(),
            'catopric': CheckboxInput(),
            'anatomical': CheckboxInput(),

        }


class SignsForm(ModelForm):
    class Meta:
        model = Signs
        fields = '__all__'
        exclude = ('user',)


class RefractionForm(ModelForm):
    class Meta:
        model = Refraction
        fields = '__all__'
        exclude = ('user',)


class CoverTestForm(ModelForm):
    class Meta:
        model = CoverTest
        fields = '__all__'
        exclude = ('user',)


class PupilReflexForm(ModelForm):
    class Meta:
        model = PupilReflex
        fields = '__all__'
        exclude = ('user',)


class PupilMeasurementForm(ModelForm):
    class Meta:
        model = PupilMeasurement
        fields = '__all__'
        exclude = ('user',)


class NewsForm(ModelForm):
    headline = forms.CharField(
        label='headline', widget=forms.CheckboxInput())

    class Meta:
        model = News
        fields = '__all__'
        exclude = ()


class OrderForm(ModelForm):

    uv400 = forms.BooleanField(initial=False,required=False)
    anti_scratch =  forms.BooleanField(initial=False,required=False)
    anti_reflective = forms.BooleanField(initial=False,required=False)
    blue_block =  forms.BooleanField(initial=False,required=False)
    frame_1_50 =  forms.BooleanField(initial=False,required=False)
    frame_Poly =  forms.BooleanField(initial=False,required=False)
    frame_1_60 =  forms.BooleanField(initial=False,required=False)
    frame_1_67 =  forms.BooleanField(initial=False,required=False)
    frame_1_74 =  forms.BooleanField(initial=False,required=False)

    class Meta:
        model = Order
        fields = '__all__'

  


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
