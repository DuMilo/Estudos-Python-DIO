linguagens = ['python', 'js', 'c', 'java', 'csharp'];

print(sorted(linguagens, key=lambda x: len(x))); # ['c', 'js', 'java', 'python', 'csharp']
print(sorted(linguagens, key=lambda x: len(x), reverse=True)); # ['python', 'csharp', 'java', 'js', 'c']

# mesma função do sort, porém ele é uma função built-in de python (não precisa colocar "linguagens.sorted").
