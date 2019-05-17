from django import forms
from .models import Image
from .widgets import FileInputWithPreview


class ImageForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = '__all__'
        widgets = {
            'file': FileInputWithPreview,
            # 次のようにすると、プレビューエレメントがウィジェットに含まれない。つまりプレビューエレメントを自分で好きな場所にかける
            # 'file': FileInputWithPreview(include_preview=False)
        }
