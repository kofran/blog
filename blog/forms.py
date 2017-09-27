from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# formulario para crear nuevos Posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'category')

# formulario para realizar comentarios en los Posts
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def clean_email(self):
        # get the email
        email = self.cleaned_data.get('email')

        # check if exist
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            #not exist
            return email
        raise forms.ValidationError('This email address is already in use.')
