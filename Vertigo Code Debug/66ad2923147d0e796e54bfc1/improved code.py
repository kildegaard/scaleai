import requests


def get_exchange_rate():
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = response.json()
    return data["rates"]["ARS"]


def ars_to_usd(amount_ars):
    exchange_rate = get_exchange_rate()
    return amount_ars / exchange_rate


def usd_to_ars(amount_usd):
    exchange_rate = get_exchange_rate()
    return amount_usd * exchange_rate


# Example usage:
amount_ars = 1000
amount_usd = ars_to_usd(amount_ars)
print(f"{amount_ars} ARS is equivalent to {amount_usd:.2f} USD")

amount_usd = 100
amount_ars = usd_to_ars(amount_usd)
print(f"{amount_usd} USD is equivalent to {amount_ars:.2f} ARS")
