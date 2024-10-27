from datetime import date, datetime, time;


data = date(2024, 10, 26);
print(data); # 2024-10-26
print(date.today()); # 2024-10-26 // data atual

data_hora = datetime(2024, 10, 26, 10, 20, 30)
print(data_hora);
print(datetime.today());

hora = time(10, 20, 30);
print(hora);