from django import forms


class answerForm(forms.Form):
    answer = forms.IntegerField(required=True)
