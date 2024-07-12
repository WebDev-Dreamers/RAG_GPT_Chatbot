from django import forms
from .models import History

# History 입력 ModelForm
class HisotryModelForm(forms.ModelForm):
    
    class Meta:
        model = History
        fields = ['question']
                  
        labels = {
            'question': '',
            'answer': 'Your Answer',
        }