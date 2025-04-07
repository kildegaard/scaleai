def convert_length(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701,
    }
    return value * (length_units[to_unit] / length_units[from_unit])


def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1000000,
        "pounds": 2.20462,
        "ounces": 35.274,
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])


# Example usage:
value_length = convert_length(100, "meters", "kilometers")
value_weight = convert_weight(1000, "grams", "pounds")


print(f"Length: {value_length} kilometers")
print(f"Weight: {value_weight} pounds")
