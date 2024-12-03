class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor;
        self.modelo = modelo;
        self.ano = ano;
        self.valor = valor;

    def buzinar(self):
        print("Bip bip!");

    def parar(self):
        print("A bicicleta estacionou.");

    def correr(self):
        print("Vrum vrum!");

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

bicicleta_1 = Bicicleta("Amarela", "Grande", "2007", "200");

bicicleta_1.buzinar()
bicicleta_1.parar()
bicicleta_1.correr()
print(bicicleta_1.__str__())