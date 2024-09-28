from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=500, required=False, widget=forms.TextInput(attrs={'placeholder': 'Write a tag', 'class': 'w-full h-8 border border-gray-300 rounded-md p-2 text-sm text-center'}))
