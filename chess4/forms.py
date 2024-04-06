from django import forms


class answerForm(forms.Form):
    what_am_i_known_as_to_people = forms.CharField(required=True)
    who_is_he = forms.CharField(required=True)

