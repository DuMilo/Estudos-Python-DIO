numeros = [1, 3, 4 , 8, 10, 11, 12];
pares = [];

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero);

print(pares); # [4, 8, 10, 12]