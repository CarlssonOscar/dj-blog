from .models import Comment
from django import forms 


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # , is needed so python does not read 'body as a string
        # instead of a tuple
        fields = ('body',)
