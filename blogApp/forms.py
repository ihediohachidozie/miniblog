from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.forms import ModelForm
from blogApp.models import Comment

class AddCommentModelForm(ModelForm):
  def clean_description(self):
    data = self.cleaned_data['description']

    # Check if description is empty.
    if len(data.strip()) == 0:
      raise ValidationError(_('Invalid comment - must contain more than one character'))

    return data 
  
  class Meta:
    model = Comment
    fields = ['description']
    help_texts = {'description': _('Enter comment about blog here.')}
