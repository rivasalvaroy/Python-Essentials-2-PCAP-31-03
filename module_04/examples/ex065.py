from datetime import datetime, timezone

print("hoy:", datetime.today())
print("ahora:", datetime.now())
# print("utc_ahora:", datetime.utcnow())
print("utc_ahora:", datetime.now(timezone.utc))
