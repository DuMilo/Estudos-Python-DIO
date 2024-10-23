#Old Style %

nome = "Milo";
idade = 19;
profissao = "estudante de Programação";
linguagem = "Python";

print("Olá, me chamo %s. Eu tenho %d anos de idade, sou %s e estou matriculado no curso de %s." % (nome, idade, profissao, linguagem));

# Saída:

# >> Olá, me chamo Milo. Eu tenho 19 anos de idade, sou estudante de Programação e estou matriculado no curso de Python.

# Método format

print("Olá, me chamo {}. Eu tenho {} anos de idade, sou {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem));

print("Olá, me chamo {3}. Eu tenho {2} anos de idade, sou {1} e estou matriculado no curso de {0}.".format(nome, idade, profissao, linguagem));

# Saída:

# >> Olá, me chamo Milo. Eu tenho 19 anos de idade, sou estudante de Programação e estou matriculado no curso de Python.
# >> Olá, me chamo Python. Eu tenho estudante de Programação anos de idade, sou 19 e estou matriculado no curso de Milo. 

# Método F-String

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, sou {profissao} e estou matriculado no curso de {linguagem}.");

# Saída:

# >> Olá, me chamo Milo. Eu tenho 19 anos de idade, sou estudante de Programação e estou matriculado no curso de Python.

# Formatar strings com F-String:

PI = 3.14159;

print(f"Valor de PI: {PI:.2f}");
print(f"Valor de PI: {PI: 10.2f}");

# Saída:

# >> Valor de PI: 3.14
# >> Valor de PI:       3.14

# Com dados pré-estabelecidos no Método Format:

dados = {"nome": "Milo", "idade": 19};

print("Nome: {nome} Idade: {idade}".format(**dados));

# Saída:

# >> Nome: Milo Idade: 19
