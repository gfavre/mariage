#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from cmsplugin_contact.forms import ContactForm


choices = ((1, 'Simple'), (2, 'Double'), (3, 'Double (lits jumeaux)'),)
class HotelForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'class': 'span6'}), required=True)
    chambre = forms.ChoiceField(choices=choices, widget=forms.RadioSelect, initial=1, required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'class': 'span6'}), required = False)
    email = forms.CharField(max_length=100, required=False)
    subject = forms.CharField(max_length=100, required=False)

    
    def clean(self):
        self.cleaned_data['email'] = 'mariage@nonoetgreg.ch'
        return self.cleaned_data