# verifica a existencia de chaves respectivas dentro do dicionario e, também, pega os valores respectivos da chave chamada.

contatos = {
    "milo@gmail.com": {"nome": "Milo", "telefone": "3333-1234"}
};

# print(contatos["chave"]); # KeyError

print(contatos.get("chave")); # None
print(contatos.get("chave", {})); # {}
print(contatos.get("milo@gmail.com", {})); # {'nome': 'Milo', 'telefone': '3333-1234'}