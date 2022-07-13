from django.forms import ModelForm
from .models import Comment


class FormComment(ModelForm):
    def clean(self):
        date = self.cleaned_data
        name = date.get('name_comment')
        email = date.get('email_comment')
        comment = date.get('comment')

        if len(name) <5:
            self.add_error(
                'name_comment',
                'name field needs more than 5 characters'
            )

    class Meta:
        model = Comment
        fields = ('name_comment', 'email_comment', 'comment')
