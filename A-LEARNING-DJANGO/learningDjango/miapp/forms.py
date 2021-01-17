
# to work with layer of abstraction for forms is better, because it bring data cleaner and offer a better validation
# it will be similar to use models, where doesn't neccessary to create html tags
# it is important to mentionate that is possible to create forms based in models

# it import allows to work with forms of Django

from django import forms

#class for validations
from django.core import validators

class FormArticle(forms.Form) :
    title = forms.CharField(
        label = 'Titulo',

        # customing form
        max_length=20,
        required=False,

        # class 237 
        # customizing widget
        # widget : a widget allows to change something visual in a field
        widget=forms.TextInput(
            attrs={
                'placeholder' : 'Mete tu titulo',
                'class': 'title_formArticle'
            }
        ),

        #setting validations
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),

                                                    # second param is a message
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'El titulo es mal formado', 'invalid_title') # 3er param is an error code
        ]
    )

    content = forms.CharField(
        label = 'Contenido',
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(50, 'Te has pasado, tu texto es muy grande') # max 20 characters
        ]
    )


    # class 237 - so I don't fat content = forms.CharField()
    content.widget.attrs.update({
        'placeholder' : 'Mete tu contenido',
        'class': 'content_formArticle',
        'id' : 'content_idForm'
    })

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