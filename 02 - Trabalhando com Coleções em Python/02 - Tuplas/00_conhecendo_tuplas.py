# diferença de lista pra tupla:
# você pode mudar o valor de listas de acordo com sua necessidade, já os valores das tuplas são imutaveis.

frutas = ("laranja", "pera", "uva", "maçã",);
# coloca-se vírgula no final para não ser confundido com uma precedência de operações
print(frutas); # ('laranja', 'pera', 'uva', 'maçã')
print(frutas[2]); # uva

letras = tuple("python");
print(letras); # ('p', 'y', 't', 'h', 'o', 'n')

numeros = tuple([1,2,3,4]);
print(numeros); # (1, 2, 3, 4)

pais = ("Brasil",);
print(pais); # ('Brasil',)


