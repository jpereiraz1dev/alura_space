from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label = 'Nome de Login',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder" : "Pedro Gabriel"
            }
        )  
    )

    senha = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder" : "Digite sua Senha"
            }
       ) 
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label = 'Nome de Cadastro',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder" : "Pedro Gabriel"
            }
        )  
    )

    email = forms.EmailField(
        label = 'Email de Cadastro',
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                "class": "form-control",
                "placeholder" : "EX: pedrogabriel@xpto.com"
            }
        )  
    )

    senha1 = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder" : "Digite sua Senha"
            }
       ) 
    )

    senha2 = forms.CharField(
        label = 'Confirme sua Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder" : "Digite sua Senha novamente"
            }
       ) 
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if  " " in nome:
                raise forms.ValidationError("Nomes de cadastro nao podem conter espacos") 
            else:
                return nome
            
    def clean_senha2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")

        if senha1 and senha2:
            if senha1 != senha2:
                raise forms.ValidationError("As senhas precisam ser iguais.")
            else:
                return senha2