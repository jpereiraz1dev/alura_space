
#TODO AULA 1 - Refatoracao e validacao

#! O bootstrap deu conflito com o stylesheet antigo

#! Entramos na pagina de login onde o bootstrap funciona perfeitamente e inspecionamos

#! Ao inspecionar copiamos a parte de style sobre os alerts

#! Abrimos a pagina de styles e colamos oq copiamos antes

#! Exclui a referencia ao bootstrap do base.html

#! Fomos ao views.py da galeria para fazer uma verificacao se a pessoa esta logada, caso nao esteja a redirecionamos pra pagina de login. Fazemos isso com o user.is_authenticated


#TODO AULA 2 - Associando tabelas

#! Criamos uma nova variavel usuario no models.py


#TODO AULA 3 - Validacao clean

#! Queremos que o nome de usuario fique sem espaco no site admin

#! Vamos ao forms.py e criamos uma funcao 'clean_nome_cadastro'

#! Utilizamos esse comando - nome = self.cleaned_data.get("nome_cadastro") - para pegar o nome_cadastro e depois fizemos uma validacao para ver se tinha espaco no nome


#TODO AULA 4 - Mensagens de erro

#! Trocamos no cadastro.html para a mensagem de erro aparecer

#! Tiramos a validacao da senha do views.py e vamos faze-la no forms 

