from django import forms
from cmsplugin_contact.forms import ContactForm


choices = ((1, 'Oui'), (0, 'Non'),)
class RSVPForm(forms.Form):
    name = forms.CharField(widget=forms.Textarea())
    presence = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
    content = forms.CharField(widget=forms.Textarea())
    
    def clean(self):
        self.cleaned_data['presence'] = int(self.cleaned_data['presence'])
        return self.cleaned_data