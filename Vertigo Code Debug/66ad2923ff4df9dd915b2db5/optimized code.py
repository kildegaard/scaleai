import pint

# Create a unit registry
ureg = pint.UnitRegistry()


def convert_length(value, from_unit, to_unit):
    quantity = value * ureg(from_unit)
    return quantity.to(to_unit).magnitude


def convert_weight(value, from_unit, to_unit):
    quantity = value * ureg(from_unit)
    return quantity.to(to_unit).magnitude


# Example:
value_length = convert_length(100, "meters", "kilometers")
value_weight = convert_weight(1000, "grams", "pounds")

print(f"Length: {value_length} kilometers")
print(f"Weight: {value_weight} pounds")
