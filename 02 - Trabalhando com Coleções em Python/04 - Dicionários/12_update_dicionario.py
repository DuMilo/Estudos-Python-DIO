# atualiza os valores das chaves dentro do dicionario.

contatos = {
    "milo@gmail.com": {"nome": "Milo", "telefone": "3333-1234"}
};

contatos.update({"milo@gmail.com": {"nome": "Mi"}});
print(contatos); # {'milo@gmail.com': {'nome': 'Mi'}}

contatos.update({"camilo@gmail.com": {"nome": "Camilo", "idade": 19}});
print(contatos); 
#{'milo@gmail.com': {'nome': 'Mi'}, 
# 'camilo@gmail.com': {'nome': 'Camilo', 'idade': 19}}