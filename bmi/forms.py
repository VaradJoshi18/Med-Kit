from .models import bmi,ideal_bmi
from django import forms

class bmiForm(forms.ModelForm):
    class Meta:
        model = bmi
        fields=['userId','age','user_weight','user_height','gender']
        
class bmiIdealForm(forms.ModelForm):
    class Meta:
        model = ideal_bmi
        fields=['age_range','gender','ideal_weight','ideal_height']