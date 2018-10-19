from django import forms


class ContactForm(forms.Form):
    fullname = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "enter your name",
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "enter your email",
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "enter your message",
    }))

    def clean_fullname(self):
        name = self.cleaned_data.get("fullname")
        if name == "sina":
            raise forms.ValidationError("sina naaaa")
        return name
