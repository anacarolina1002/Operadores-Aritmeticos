
#mostrar mensagem na tela
print("Eu não aguento mais")
print('socorro')

#declaração de variável
numeroInteiro = 2
numeroDecimal = 2.4456
palavraCaractereDupla = "Ana"
palavraCaractereSimples = 'Carolina'
verdadeiroFalso = True

#mostrar no terminal os valores atribuidos as variáveis
print(numeroInteiro)
print(numeroDecimal)
print(palavraCaractereDupla)
print(palavraCaractereSimples)
print(verdadeiroFalso)

#informar o tipo de dado que a variável armazena
print(type(numeroInteiro))
print(type(numeroDecimal))
print(type(palavraCaractereDupla))
print(type(palavraCaractereSimples))
print(type(verdadeiroFalso))

#recursos para dados de tipo string
#len conta a quantidade de de caracteres de uma variável
print(len(palavraCaractereDupla))
print(len(palavraCaractereSimples))
#repetir o valor da variável
print(palavraCaractereDupla * 3)
#concatenando strings
print(palavraCaractereDupla +" ",palavraCaractereSimples)
#recursos para dados tipo float
print(numeroDecimal)
print(round(numeroDecimal,2))
#casas depois da vírgula sem arredondar
print("%.2f" % (numeroDecimal))
