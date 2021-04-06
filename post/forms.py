from .models import Comment, Contact
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        exclude=('post','created_by','active','parent')
        widgets = {
            'content' : forms.Textarea(attrs={'class':'form-control','placeholder':'Content'}),       
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'Content','phone')
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email' : forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'Content' : forms.Textarea(attrs={'class':'form-control','placeholder':'Content'}),
            'phone' : forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'})
            
        }
