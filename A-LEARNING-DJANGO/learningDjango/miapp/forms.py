
# to work with layer of abstraction by forms is better, because it bring data cleaner and offer a better validation
# it will be similar to use models, where doesn't neccessary to create html tags

# it import allows to work with forms of Django

# it is important to mentionate that is posible to create forms based in models
from django import forms

class FormArticle(forms.Form) :
    title = forms.CharField(
        label = 'Titulo'
    )

    content = forms.CharField(
        label = 'Contenido',
        widget=forms.Textarea
    )

    # creating select for form
    public_options = [
        # options for tag select
        (1, 'Si'), 
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label = '¿Publicado?',
        choices = public_options
    )