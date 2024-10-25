contatos = {
    "milo@gmail.com": {"nome": "Milo", "telefone": "3333-1234"},
    "george@gmail.com": {"nome": "George", "telefone": "3443-1234"},
    "carla@gmail.com": {"nome": "Carla", "telefone": "3214-3567"},
};

for chave in contatos:
    print(chave, contatos[chave]);
# milo@gmail.com {'nome': 'Milo', 'telefone': '3333-1234'}
# george@gmail.com {'nome': 'George', 'telefone': '3443-1234'}
# carla@gmail.com {'nome': 'Carla', 'telefone': '3214-3567'}

for chave, valor in contatos.items():
    print(chave, valor);
# milo@gmail.com {'nome': 'Milo', 'telefone': '3333-1234'}
# george@gmail.com {'nome': 'George', 'telefone': '3443-1234'}
# carla@gmail.com {'nome': 'Carla', 'telefone': '3214-3567'}