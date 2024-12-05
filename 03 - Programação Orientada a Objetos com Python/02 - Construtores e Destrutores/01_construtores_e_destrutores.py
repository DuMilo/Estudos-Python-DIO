class Teste:
    def __init__(self):
        print("Iniciei esta classe!");

    def __del__(self):
        print("Destruindo a instância :(");
    
instancia = Teste();
del instancia;