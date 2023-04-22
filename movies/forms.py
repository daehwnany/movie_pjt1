from django import forms
from .models import Movie, Comment


class MovieForm(forms.ModelForm):

    # 영화 세부내용 폼 
    select = [
        ('comedy', 'comedy'),
        ('thriller', 'thriller'),
        ('romance', 'romance'),
        ('action', 'action'),
        ('horror', 'horror'),
        ('fantasy', 'fantasy'),
        ('musical', 'musical'),
    ]
    genre = forms.ChoiceField(choices = select)
    score = forms.FloatField(required=False, max_value=5, min_value=0,widget=forms.NumberInput(attrs={'step':'0.5'}))
    release_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Movie
        exclude = (
            'user',
            'like_users',
        )


class CommentForm(forms.ModelForm):
    

    class Meta:
        model = Comment
        fields = ('content',)

    