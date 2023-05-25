from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        for name, field in self.fields.items():
            print(name)
            field.widget.attrs.update({"class": "text"})

    class Meta:
        model = Book
        fields = '__all__'