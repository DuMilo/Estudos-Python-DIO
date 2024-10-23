numeros = {1, 2, 3, 1, 4, 5, 2, 6, 7, 8, 9, 0};

print(numeros); # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.remove(0); # 0
print(numeros); # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# diferença com o discard:
# se o elemento existe com o 'remove', ele descarta. se não, o código dá erro.
# se o elemento existe com o 'discard', ele descarta. se não, o código continua funcionando.