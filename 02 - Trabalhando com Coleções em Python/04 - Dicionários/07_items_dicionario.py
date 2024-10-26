# itera as chaves e seus valores dentro do dicionario

contatos = {
    "milo@gmail.com": {"nome": "Milo", "telefone": "3333-1234"},
    "george@gmail.com": {"nome": "George", "telefone": "3443-1234"},
    "carla@gmail.com": {"nome": "Carla", "telefone": "3214-3567"},
};

print(contatos.items());
# dict_items([('milo@gmail.com', {'nome': 'Milo', 'telefone': '3333-1234'}), 
# ('george@gmail.com', {'nome': 'George', 'telefone': '3443-1234'}), 
# ('carla@gmail.com', {'nome': 'Carla', 'telefone': '3214-3567'})])