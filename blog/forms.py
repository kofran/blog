from django import forms
from .models import Post, Comment

# formulario para crear nuevos Posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')

# formulario para realizar comentarios en los Posts
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
