# remove uma chave de dentro do dicionario

contatos = {
    "milo@gmail.com": {"nome": "Milo", "telefone": "3333-1234"},
    "george@gmail.com": {"nome": "George", "telefone": "3443-1234"},
    "carla@gmail.com": {"nome": "Carla", "telefone": "3214-3567"},
};

print(contatos.pop("milo@gmail.com", )); 
# {'nome': 'Milo', 'telefone': '3333-1234'}
print(contatos.pop("milo@gmail.com", "Não existem valores."));
print(contatos.items());
# dict_items([('george@gmail.com', {'nome': 'George', 'telefone': '3443-1234'}),
# ('carla@gmail.com', {'nome': 'Carla', 'telefone': '3214-3567'})])