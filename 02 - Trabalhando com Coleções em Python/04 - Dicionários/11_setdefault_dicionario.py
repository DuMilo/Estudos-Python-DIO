# adiciona chaves e valores, mas não modifica chaves já criadas.

contato = {"nome": "Milo", "sobrenome": "Moreira"};

print(contato.setdefault("nome", "Camilo")); # Milo
print(contato); # {'nome': 'Milo', 'sobrenome': 'Moreira'}

print(contato.setdefault("idade", "19")); # 19
print(contato); # {'nome': 'Milo', 'sobrenome': 'Moreira', 'idade': '19'}