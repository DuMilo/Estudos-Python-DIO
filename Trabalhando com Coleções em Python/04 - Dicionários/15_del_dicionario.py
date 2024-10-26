contatos = {
    "milo@gmail.com": {"nome": "Milo", "telefone": "3333-1234"},
    "george@gmail.com": {"nome": "George", "telefone": "3443-1234"},
    "carla@gmail.com": {"nome": "Carla", "telefone": "3214-3567"},
};

del contatos["milo@gmail.com"]["telefone"];
del contatos["carla@gmail.com"];

print(contatos);
# {'milo@gmail.com': {'nome': 'Milo'}, 
# 'george@gmail.com': {'nome': 'George', 'telefone': '3443-1234'}}