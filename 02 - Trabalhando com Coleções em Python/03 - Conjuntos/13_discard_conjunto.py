# para descartar/retirar números de um set.

numeros = {1, 2, 3, 1, 4, 5, 2, 6, 7, 8, 9, 0};
# retira os repetidos para depois aplicar discard.

print(numeros); # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.discard(1);
numeros.discard(45);
print(numeros); # {0, 2, 3, 4, 5, 6, 7, 8, 9}