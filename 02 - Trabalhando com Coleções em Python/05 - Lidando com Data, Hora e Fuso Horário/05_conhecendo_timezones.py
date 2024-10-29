from datetime import datetime;
import pytz; # pip install pytz no terminal

data = datetime.now(pytz.timezone("America/Sao_Paulo"));

print(data.strftime("%d/%m/%Y, %H:%M"));
# 28/10/2024, 21:43