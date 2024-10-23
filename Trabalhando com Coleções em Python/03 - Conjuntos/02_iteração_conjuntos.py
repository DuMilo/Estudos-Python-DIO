carros = {"gol", "celta", "palio"};

for carro in carros:
  print(carro);

# celta
# palio
# gol
  
# Função Enumerate

for indice, carro in enumerate(carros):
  print(f"[{indice}]: {carro}");
  
#[0]: celta
#[1]: palio
#[2]: gol