VOGAIS = "aeiouAEIOU";
contador = 0;

def conta_vogais(texto):
    global contador;
    
    for letra in texto:
        if letra in VOGAIS:
            contador += 1;
    return contador;

texto = input("");

resultado = conta_vogais(texto);
print(f"O número de vogais na string '{texto}' é: {resultado}");