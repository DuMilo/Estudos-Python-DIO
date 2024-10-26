contatos = {
    "milo@gmail.com": {"nome": "Milo", "telefone": "3333-1234"}
};

copia = contatos.copy();
copia["milo@gmail.com"] = {"nome": "Mi"}; # só foi colocado o valor de nome, então só aparecerá ele aqui

print(contatos["milo@gmail.com"]); # {'nome': 'Milo', 'telefone': '3333-1234'}
print(copia["milo@gmail.com"]); # {'nome': 'Mi'}
