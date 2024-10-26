carros = ("gol", "celta", "palio",);

for carro in carros:
    print(carro);

# gol
# celta
# palio

# Por Enumerate

for indice, carro in enumerate(carros):
    print(f"[{indice}]: {carro}");

# [0]: gol
# [1]: celta
# [2]: palio
