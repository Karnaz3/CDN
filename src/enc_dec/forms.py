from django import forms

class EncryptionForm(forms.Form):
    text = forms.CharField(label='Enter the text:', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=True)
    image = forms.ImageField(label='Upload an image:', widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=True)

class DecryptionForm(forms.Form):
    image = forms.ImageField(label='Upload the encrypted image:', widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}), required=True)