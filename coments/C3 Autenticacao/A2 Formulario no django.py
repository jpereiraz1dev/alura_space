
#TODO AULA 1 - Criando formularios

#! Fomos na posta usuarios e criamos o arquivo forms.py

#! Nesse arquivo, fazemos algo parecido com o feito no models para ter o padrao do nosso formulario e criamos uma classe chamada LoginForms

#! Importamos esse form no views do usuarios

#! Fomos ao login.html e tiramos o modelo de login hardcode e introduzimos o csrftoken apos a tag de formulario

#! Introduzimos um for no login.html para nosso formulario ficar visivel na pagina web


#TODO AULA 2 - Estilizando formularios

#! Criamos uma nova div e nela colocamos o botao de submit

#! Colocamos na pagina html as seguintes atribuicoes: 
#*     DIV GERAL:
#       - class="col-12 col-lg-12"
#       - style="margin-bottom: 10px;" 

#*     LABEL
#       - style="color:#D9D9D9; margin-bottom: 5px;"

#*     BUTTON
#       - class="btn btn-success col-12"
#       - style="padding: top 5px;"

#! Voltamos ao forms.py e nele adicionamos uma widget para cada variavel na class e nela conseguimos fazer atribuicoes de estilo


#TODO AULA 3 - Formularios de cadastro

#! Fazemos outra classe no forms.py, essa chamada CadastroForms

#! Importamos a classe no views.py e dps substituimos no html assim como feito pro login


#TODO AULA PSM - CSRF

#! O CSRF Token eh necessario para ter mais seguranca nas aplicacoes webs e sites, pois ele impede que hackers consigam utilizar seu token de autenticacao ao trocar o mesmo por caracteres aleatorios
