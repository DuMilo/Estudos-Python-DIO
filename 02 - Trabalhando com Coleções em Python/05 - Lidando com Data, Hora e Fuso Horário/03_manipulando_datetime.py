from datetime import datetime, timedelta, date;

print(date.today() - timedelta(days=1));
# 2024-10-25 // data atual - 1

# não é possível dar time.today() ou time.now(), então podemos fazer isso:

horas = datetime.today() - timedelta(hours=1);
print(horas.time());
# 21:23:29.311611

print(datetime.now().date());
# 2024-10-26 
print(date.today());
# 2024-10-26