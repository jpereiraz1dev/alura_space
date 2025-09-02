
#! app sao as aplicacacoes, enquanto project eh a base

#! eh preciso inserir cada app nas settings do setup

#* Para carregar arquivos estaticos, precisa incluir essas configuracoes nas settings 
'''
-- STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
 ]

--  STATIC_ROOT = os.path.join(BASE_DIR, 'static') '''


#* *Boas Praticas*
'''
- Separar as urls em categorias
- Criar uma lista para manter todos os endpoints da nossa aplicacao relacionado a cada categoria
'''

#! DRY - Don't Repeat Yourself

#!Quando precisa utilizar o DRY, faz-se uma base.html para evitar as repeticoes no codigo, isso pras coisas principais mas para funcoes se cria uma pasta partials e dentro dela um arquivo '_footer.html' e no base.html utilizar {% include '/partials/_footer.html' %}