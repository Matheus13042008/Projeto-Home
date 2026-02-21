print('Formulário')
nome = input('Digite seu Nome:\n')
sobrenome = input('Digite seu sobrenome:\n')
print('Confirma Que Seu Nome Então É:', (nome.upper()), (sobrenome.upper()))
nascimento = input('Digite quando você nasceu, incluindo dia, mês e ano:\n')
universidade = input('Digite qual universidade está cursando:\n')

email = (nome.lower()) + '.' + (sobrenome.lower()) + '@' + (universidade.lower()) +'.br'
print('Seu email é:',email)
print('Sua senha é:''a' + str(email.count('a')) + 'e' + str(email.count('e')) + 'i' + str(email.count('i')) + 'o' + str(email.count('o')) + 'u' + str(email.count('u')))
