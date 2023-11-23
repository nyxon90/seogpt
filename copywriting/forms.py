from django import forms


class MyForm(forms.Form):
    input_text = forms.CharField(label='Введите текст', max_length=500)


class InputKeywords(forms.Form):
    input_text = forms.CharField(label='Введите ключевые слова', max_length=1000)

