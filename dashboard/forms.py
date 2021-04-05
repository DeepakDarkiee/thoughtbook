from post.models import Post
from django import forms

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class PostForm(forms.ModelForm):  
    class Meta:
        model = Post
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'slug' : forms.TextInput(attrs={'class':'form-control','placeholder':'Slug'}),
            'content' : forms.Textarea(attrs={'class':'form-control','placeholder':'Content'}),
            'status' : forms.Select(choices = STATUS,attrs={'class':'form-control','placeholder':'Status'}),
            
        }
        fields = "__all__"
        exclude = ('author','slug')



    # title = forms.CharField( max_length=100 , widget=forms.TextInput(attrs={'class': "form-control",'placeholder':'Title'}))
     
    # slug = forms.CharField( max_length=100 , widget=forms.TextInput(attrs={'class': "form-control",'placeholder':'Slug'}))

    # content = forms.CharField( max_length=1000 , widget=forms.Textarea(attrs={'class': "form-control",'placeholder':'Content'}))

    # status = forms.ChoiceField(choices = STATUS,widget=forms.Select(attrs={'class':'form-control'}))
   