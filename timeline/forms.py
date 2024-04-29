from django import forms
from .models import *
 
class timelineForm(forms.ModelForm):
    class Meta:
        model = timeline
        fields=['userId','update']
        
class user_timeline_edit_Form(forms.ModelForm):
    class Meta:
        model = timeline
        fields=['userId','update']
        
class timeline_docForm(forms.ModelForm):
    class Meta:
        model = timeline_doc
        fields=['docId','update']
        
class timeline_pharmaForm(forms.ModelForm):
    class Meta:
        model = timeline_pharma
        fields=['pharmaId','update']        
