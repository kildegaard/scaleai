def normalize_product_info(product_info):
    # Normalize product names and SKUs by removing extra spaces and converting to lowercase
    product_info["name"] = product_info["name"].strip().lower()
    product_info["sku"] = product_info["sku"].strip().lower()
    return product_info


def generate_skus(product_info):
    # Generate possible SKUs for each product name based on different patterns
    name = product_info["name"]
    product_id = product_info["id"]

    # Calculate the sum and multiplication of the product ID digits
    id_sum = sum(int(digit) for digit in str(product_id))
    id_multiply = 1
    for digit in str(product_id):
        id_multiply *= int(digit)

    # Generate possible SKUs
    possible_skus = []

    # For one-word product names
    if len(name.split()) == 1:
        sku = name[:3] + str(id_sum)
        possible_skus.append(sku)

    # For two-word product names
    elif len(name.split()) == 2:
        words = name.split()
        sku = words[0][0] + words[1][0] + str(id_multiply)
        possible_skus.append(sku)

    # For three-word product names
    elif len(name.split()) == 3:
        words = name.split()
        sku = words[0][0] + words[1][0] + words[2] + str(product_id)
        possible_skus.append(sku)

    return possible_skus


# Example usage
product_info_list = [
    {"id": 123, "name": " Product A", "sku": " Unknown"},
    {"id": 456, "name": "Product B ", "sku": "Unknown "},
    {"id": 789, "name": " Product C", "sku": " Unknown"},
]

normalized_product_info_list = [
    normalize_product_info(product_info) for product_info in product_info_list
]
generated_skus = [
    generate_skus(product_info) for product_info in normalized_product_info_list
]

for i, product_info in enumerate(normalized_product_info_list):
    print(f"Product Name: {product_info['name']}, Possible SKUs: {generated_skus[i]}")
