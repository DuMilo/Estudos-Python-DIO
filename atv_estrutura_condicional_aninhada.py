def sacar(valor):
    saldo = 500;

    if (saldo >= valor):
        print("Valor sacado!");
    elif (saldo < valor):
        print("Valor inválido...");

saque = float(input("Valor do saque:\n"));
sacar(saque);