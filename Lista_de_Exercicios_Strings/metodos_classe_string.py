nome = "MiLO mOrEirA";

print(nome.upper());
print(nome.lower());
print(nome.title());

texto = "   Oba, amanhã tem bolo   ";

print(texto + "!");
print(texto.strip() + "!");
print(texto.lstrip() + "!");
print(texto.rstrip() + "!");

menu = "Python";

print("####" + menu + "####");
print(menu.center(14));
print(menu.center(14,"#"));
print("P-y-t-h-o-n");
print("-".join(menu));

# Como fazer por iteração (loop);

for letra in menu:
    print(letra, end=".");

# Qualquer nome que for inserido em 'letra', automaticamente já vai ser referir
# ao caracteres da String.