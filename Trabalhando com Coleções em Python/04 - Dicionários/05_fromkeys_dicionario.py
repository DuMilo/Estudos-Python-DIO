# adição de chaves a um dicionario

print(dict.fromkeys(["nome", "telefone"]));
# {'nome': None, 'telefone': None}

print(dict.fromkeys(["nome", "telefone"], "vazio"));
# {'nome': 'vazio', 'telefone': 'vazio'}