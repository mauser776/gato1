from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    correo = forms.EmailField(label='Correo', widget=forms.EmailInput(
        attrs={'class': 'form-control'}
    ))
    mensaje = forms.CharField(label='Mensaje', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 6,
        'style': 'resize:none;',
        'placeholder': 'Escribe tu mensaje aquí...'
    }))
