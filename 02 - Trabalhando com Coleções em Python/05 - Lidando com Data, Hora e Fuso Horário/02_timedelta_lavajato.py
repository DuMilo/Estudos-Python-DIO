from datetime import datetime, timedelta;

tipo_carro = 'P'; # P, M, G

tempo_pequeno = 30;
tempo_medio = 45;
tempo_grande = 60;
data_atual = datetime.now();

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno);
    print(f"Sua lavagem estará completa às {data_estimada}!");
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio);
    print(f"Sua lavagem estará completa às {data_estimada}!");
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande);
    print(f"Sua lavagem estará completa às {data_estimada}!");