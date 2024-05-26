# Sample data (replace with your actual data)
product_data = [
    {"id": 123, "name": " apple", "sku": ""},
    {"id": 456, "name": "samsung galaxy", "sku": ""},
    {"id": 789, "name": "Google pixel 3XL", "sku": ""},
]


def normalize_string(s):
    return s.strip().lower()


def generate_sku(name, product_id):
    words = name.split()
    if len(words) == 1:
        sku = words[0][:3] + str(sum(int(digit) for digit in str(product_id)))
    elif len(words) == 2:
        sku = "".join(word[0] for word in words) + str(eval("*".join(str(product_id))))
    else:  # 3 or more words
        sku = words[0][0] + words[1][0] + words[-1] + str(product_id)
    return sku


for product in product_data:
    product["name"] = normalize_string(product["name"])
    product["sku"] = generate_sku(product["name"], product["id"])

for product in product_data:
    print(product)
