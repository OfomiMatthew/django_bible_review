from django.forms import ModelForm, Textarea
from .models import *

class ReviewForm(ModelForm):
  def __init__(self,*args,**kwargs):
    super(ModelForm,self).__init__(*args,**kwargs)
    self.fields['text'].widget.attrs.update({'class':'form-control'})
    self.fields['studyAgain'].widget.attrs.update({'class':'form-check-input'})
    
  class Meta:
      model = Review
      fields = ['text','studyAgain']
      labels = {
        'studyAgain':('Study Again'),
        'text':('Comment'),
      }
      widgets = {
        'text':Textarea(attrs={'rows':4}),
      }
  