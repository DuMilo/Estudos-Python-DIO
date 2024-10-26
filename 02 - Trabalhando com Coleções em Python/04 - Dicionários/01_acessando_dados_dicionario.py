dados = {'nome': 'Milo', 'idade': 19, 'telefone': '3333-1234'}

print(dados['nome']); # "Milo"
print(dados['idade']); # 19
print(dados['telefone']); # "3333-1234"

dados['nome'] = "Camilo" ;
dados['nome'] = 20 ;
dados['nome'] = "9988-1781"; 

print(dados); # {'nome': '9988-1781', 'idade': 19, 'telefone': '3333-1234'}