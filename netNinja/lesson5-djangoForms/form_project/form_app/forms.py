from django import forms
class contantForm(forms.Form):
       name=forms.CharField(max_length=100)
       email=forms.EmailField()
       message=forms.CharField(widget=forms.Textarea)
       def sendEmail(self):
           return(f"sending email from {self.cleaned_data['email']} with message: {self.cleaned_data['message']}")
               
