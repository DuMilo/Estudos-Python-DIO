# para saber se os elementos de um certo conjunto/set estão inseridos em outro set.

conjunto_a = {1,2,3};
conjunto_b = {4,1,2,5,6,3};

print(conjunto_a.issubset(conjunto_b)); # True
print(conjunto_b.issubset(conjunto_a)); # False