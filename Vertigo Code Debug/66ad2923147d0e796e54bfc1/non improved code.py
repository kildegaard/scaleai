def ars_to_usd(amount_ars, exchange_rate):
    amount_usd = amount_ars / exchange_rate
    return amount_usd


def usd_to_ars(amount_usd, exchange_rate):
    amount_ars = amount_usd * exchange_rate
    return amount_ars


# exchange rate from ARS to USD
exchange_rate = 1350


# examples

amount_ars = 1000
amount_usd = ars_to_usd(amount_ars, exchange_rate)
print(f"{amount_ars} ARS is equivalent to {amount_usd:.2f} USD")

amount_usd = 100
amount_ars = usd_to_ars(amount_usd, exchange_rate)
print(f"{amount_usd} USD is equivalent to {amount_ars:.2f} ARS")
