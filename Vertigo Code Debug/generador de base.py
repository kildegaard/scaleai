import pandas as pd
import faker

# Create an instance of the Faker class
fake = faker.Faker()

# Create a list of dictionaries with fake data
data = []
for _ in range(15):
    record = {
        "name": fake.name(),
        "address": fake.address(),
        "age": fake.random_int(min=18, max=80),
        "email": fake.email(),
        "amount_spent": round(fake.random_number(digits=5, fix_len=True) / 100, 2),
    }
    data.append(record)

# Convert the list of dictionaries to a DataFrame
df = pd.DataFrame(data)
df

# export to a csv file

df.to_csv("data.csv", index=False)
