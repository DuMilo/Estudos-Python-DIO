from datetime import datetime;

data = datetime.now();

# para formatar data e hora (não aparecer segundos nem milésimos)
print(data.strftime("%d/%m/%Y %H:%M"));
# 28/10/2024 20:44

# para converte string para datetime
data_string = "28/10/2024 20:44";
data = datetime.strptime(data_string, "%d/%m/%Y %H:%M");
print(data);
# 2024-10-28 20:44:00
