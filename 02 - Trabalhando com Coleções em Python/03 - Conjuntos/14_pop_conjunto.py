numeros = {1, 2, 3, 1, 4, 5, 2, 6, 7, 8, 9, 0};

print(numeros); # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.pop(); # 0  
numeros.pop(); # 1
print(numeros); # {2, 3, 4, 5, 6, 7, 8, 9}

# no caso de conjuntos, o pop tirará o valor da frente e não o último valor da lista como de costume.