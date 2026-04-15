# Calculates exchange rates between a base currency (USD) and 3 African currencies
usd_amount = 50

# Fictional exchange rates against the USD for demonstration
ngn_rate = 1150.50  # Nigerian Naira
zar_rate = 18.90    # South African Rand
kes_rate = 130.20   # Kenyan Shilling

# Calculations using variables and operators
ngn_total = usd_amount * ngn_rate
zar_total = usd_amount * zar_rate
kes_total = usd_amount * kes_rate

print(f"${usd_amount} USD is equivalent to:")
print(f"- {ngn_total:.2f} Nigerian Naira (NGN)")
print(f"- {zar_total:.2f} South African Rand (ZAR)")
print(f"- {kes_total:.2f} Kenyan Shilling (KES)")
