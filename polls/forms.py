from django import forms

from polls.models import Question
   
# creating a form 
class InputForm(forms.Form, question: Question):
    for choice in question.choice_set.all:
        q = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)