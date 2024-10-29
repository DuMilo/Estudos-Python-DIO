from datetime import datetime, timezone, timedelta;

data_oslo = datetime.now(timezone(timedelta(hours=2)));
data_sp = datetime.now(timezone(timedelta(hours=-3)));

print(data_oslo);
print(data_sp);
# 2024-10-29 03:36:27.263961+02:00
# 2024-10-28 22:36:27.263961-03:00