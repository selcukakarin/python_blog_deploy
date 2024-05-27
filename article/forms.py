from django import forms
from .models import Article
from tinymce.widgets import TinyMCE

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = "__all__"
        exclude = ["author"]
        widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}
