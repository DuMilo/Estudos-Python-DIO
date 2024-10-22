linguagens = ['python', 'js', 'c', 'java', 'csharp'];
linguagens.sort();
print(linguagens); # ['c', 'csharp', 'java', 'js', 'python']

linguagens = ['python', 'js', 'c', 'java', 'csharp'];
linguagens.sort(reverse=True);
print(linguagens); # ['python', 'js', 'java', 'csharp', 'c']

linguagens = ['python', 'js', 'c', 'java', 'csharp'];
linguagens.sort(key=lambda x: len(x));
print(linguagens); # ['c', 'js', 'java', 'python', 'csharp']

linguagens = ['python', 'js', 'c', 'java', 'csharp'];
linguagens.sort(key=lambda x: len(x), reverse=True);
print(linguagens); # ['python', 'csharp', 'java', 'js', 'c']

numeros = [3, 4 , 1, 10, 13, 6, 74, 13];
numeros.sort();
print(numeros); # [1, 3, 4, 6, 10, 13, 13, 74]