
#TODO AULA 1 - Usuario no Django

#! Trocamos nas paginas html o metodo que antes estava vazio para POST e action para um redirecionamento

#! Voltamos nas views.py e importamos um novo metodo do django, o 'redirect'.

#! Criamos uma condicao para ver se a senha 1 e 2 sao diferentes


#TODO AULA 2 - Logica de Cadastro

#! Nas views.py importamos do django.contrib.auth.models os Users

#! Checamos se o formulario eh valido e caso seja atribuimos as informacoes passadas a variaveis utilizando o form['nome_da_variavel'].value ()

#! Utilizamos o User.objects.filter(parametro)exists() para ver se aquele nome de usuario ja existe no banco de dados e caso nao exista utilizamos o User.objects.create_user(parametros) para cria-lo no banco de dados

#! Apos isso, damos um usuario.save() e redirecionamos para a pagina 'login'


#TODO AULA 3 - Logica de Login

#! Importamos do django.contrib o auth no views.py

#! criamos uma variavel usuario que recebe auth.authenticate(request, username = nome, password = senha)

#! Criamos um if pra ver se o sistema achou alguem com aquele usuario


#TODO AULA 4 - Alertas e mensagens

#! Da django.contrib importamos o messages no views.py

#! Utilizamos messages.success(request,'mensagem') para mensagens positivas e messages.error() pra negativas

#! Trocamos nas paginas html para as mensagens serem vistas, e fazemos isso a partir de um for
 

#TODO AULA 5 - Logout

#! Criamos uma nova funcao chamada logout

#! Nessa funcao damos um auth.logout(request)

#! Adicionamos a funcao logout no urls.py