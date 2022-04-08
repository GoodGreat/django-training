from django import forms

from polls.models import Question
   
# creating a form 
class InputForm(forms.Form):

    def __init__(self, question: Question):
        cf = forms.ChoiceField(choices=question.choice_set.all, widget=forms.RadioSelect)
        
