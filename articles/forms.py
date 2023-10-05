from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder': '기가막힌제목',
                'maxlength': 10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
                'placeholder': '놀라운내용',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '빈내용은 안돼!!!'
        }
    )

    class Meta:
        model = Article
        fields = '__all__'