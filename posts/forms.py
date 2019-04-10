from django import forms
from .models import Post


class PostModelForm(forms.ModelForm):
    content = forms.CharField(label='content')
    
    class Meta:
        model = Post
        # input을 만들 칼럼 값을 list로 만들어 넣어준다.
        fields = ['content',]
        widget = {
            'content': forms.Textarea(attrs={
                'class': '',
                'rows' : 5,
                'cols' : 50,
                'placeholder' : "지금 뭘 하고 계신가요 ?",
            })
        }
        