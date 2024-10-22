numeros = [1, 3, 4 , 8, 10, 11, 12];
pares = [numero for numero in numeros if numero % 2 == 0]; 
# o primeiro numero é para fazer o append (armazenar os valores na lista), o resto é sintaxe normal in one line.

print(pares); # [4, 8, 10, 12]

pares = [numero % 2 == 0 for numero in numeros];
# já aqui ele apresenta um valor booleano para os numeros, sendo true pra par e false pra impar.

print(pares); # [False, False, True, True, True, False, True]