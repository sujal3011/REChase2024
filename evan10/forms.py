from django import forms


class answerForm(forms.Form):
    answer = forms.CharField(max_length=11,required=True)
