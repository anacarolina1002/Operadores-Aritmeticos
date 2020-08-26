#Variáveis
numeroX = 2
numeroY = 3

#Operadores Aritméticos
#Soma
resposta = numeroX + numeroY
#Mostrar a resposta método 1
print("A resposta equivale a:",resposta)
#Mostrar a resposta método 2
print("A resposta equivale a:",(numeroX + numeroY))
#No método acima, não se pode usar o resultado em
#outros comandos, pois o valor não foi atribuido a
#uma variável específica

#Subtração
respostaSubtracao = numeroX - numeroY
#Mostrar a resposta método 1
print("O valor da subtração é:",respostaSubtracao)
#Mostrar a resposta método 2
print("O valor da subtração é:", (numeroX - numeroY))
#No método acima, não se pode usar o resultado em
#outros comandos, pois o valor não foi atribuido a
#uma variável específica

#Multiplicação
respostaMultiplicacao = numeroX * numeroY
#Mostrar a resposta método 1
print("O valor da multiplicação é:",respostaMultiplicacao)
#Mostrar a resposta método 2
print("O valor da multiplicação é:", (numeroX * numeroY))
#No método acima, não se pode usar o resultado em
#outros comandos, pois o valor não foi atribuido a
#uma variável específica
#Mostrar a resposta método 3 (Preguiça)
meuTexto = "A resposta da multiplicação é:"
print(meuTexto,(numeroX * numeroY))

#Divisão
respostaDivisao = numeroX / numeroY
#Mostrar a resposta método 1
print("O valor da divisão é:",respostaDivisao)
#Mostrar a resposta método 2
print("O valor da divisão é:", (numeroX / numeroY))
#No método acima, não se pode usar o resultado em
#outros comandos, pois o valor não foi atribuido a
#uma variável específica

#Expoente
respostaExpoente = numeroX ** numeroY
#Mostrar a resposta método 1
print("O valor do expoente é:",respostaExpoente)
#Mostrar a resposta método 2
print("O valor do expoente é:", (numeroX ** numeroY))
#No método acima, não se pode usar o resultado em
#outros comandos, pois o valor não foi atribuido a
#uma variável específica

#Operadores Lógicos e Relacionais
print("Operador lógico AND(e)",(numeroX <5 and numeroY < 10))
print("Operador lógico OR(ou)",(numeroX < 5 or numeroY > 20))
print("Operador lógico de NEGAÇÃO(não)", (not(numeroX < 5 and numeroY < 10)))
print("Operador relacional != (diferente):",(numeroX != numeroY))

#Usando input para ler dado de tipo String(str) do teclado
armazenaValorTecladoString = (input("Digite um valor:"))
print("O tipo de dado é:",type(armazenaValorTecladoString))
print("O valor digitado foi:",(armazenaValorTecladoString))

#Usando input para ler dado de tipo Inteiro(int) do teclado
armazenaValorTecladoInt = input("Digite um valor inteiro:")
print("O tipo de dado é:",type(armazenaValorTecladoInt))
print("O valor inteiro é:",(armazenaValorTecladoInt))

#Usando input para ler dado de tipo Float do teclado
armazenaValorTecladoFloat = input("Digite um valor real: (Ex: 2.50)")
print("O tipo de dado:",type(armazenaValorTecladoFloat))
print("O valor float é:",armazenaValorTecladoFloat)







