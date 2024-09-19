VOGAIS = "AEIOU"

while True:
    texto = input("Informe um texto (ou 'pare' para sair): ")
    
    if texto.lower() == 'pare' or 'stop':
        break

    for letra in texto:
        if letra.upper() in VOGAIS:
            print(letra, end=" ")
    
    print()  # Para pular para a próxima linha após imprimir as vogais
