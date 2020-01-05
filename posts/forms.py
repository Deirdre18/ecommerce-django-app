from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = Post
        # don't have created date or user edible views, as these are only form fields that user can edit.
        fields = ('title', 'content', 'image', 'tag', 'published_date')
