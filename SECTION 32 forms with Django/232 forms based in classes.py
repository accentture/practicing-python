""" 
--example to create fields in a form : 

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
 """