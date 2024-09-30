
from django import forms
from posts.models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        models = Comment
        fields = ['text']
class PostForm(forms.ModelForm):
    image = forms.ImageField()
    title = forms.CharField(max_length=100)
    content = forms.CharField()

def clean_title(self):
    title = self.cleaned_data.get('title')
    if title.lower() == "python":
        raise forms.ValidationError("title can't be python")
    else:
        return title

def clean(self):
    cleaned_data = super().clean()
    title = cleaned_data.get('title')
    content = cleaned_data.get('content')
    if title.lower() == content.lower():
        raise forms.ValidationError("title and content must be different")


class PostForm2(forms.ModelForm):
    class Meta:
        models = Post
        fields = ['title', 'content', 'image']

def clean_title(self):
    title = self.cleaned_data.get('title')
    if title.lower() == "python":
        raise forms.ValidationError("title can't be python")
    else:
        return title

def clean(self):
    cleaned_data = super().clean()
    title = cleaned_data.get('title')
    content = cleaned_data.get('content')
    if title.lower() == content.lower():
        raise forms.ValidationError("title and content must be different")
