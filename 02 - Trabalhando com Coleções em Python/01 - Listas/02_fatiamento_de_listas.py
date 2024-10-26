lista = ["p","y", "t", "h", "o", "n"];

print(lista[2:]); # [ "t", "h", "o", "n"]
print(lista[:2]); # [ "p", "y" ]
print(lista[1:3]); # [ "y" , "t" ]
print(lista[0:3:2]); # [ "p" , "t" ] nessa questão, 0:3:2, o primeiro elemento diz onde começar, o segundo elemento diz onde parar, já o terceiro diz de quanto em quanto vai "pular"
print(lista[::]); # ["p","y", "t", "h", "o", "n" ] 
print(lista[::-1]); # [ 'n', 'o', 'h', 't', 'y', 'p' ]