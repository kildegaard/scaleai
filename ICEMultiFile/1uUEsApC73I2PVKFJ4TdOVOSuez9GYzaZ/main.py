import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)

# Read the CSV file into a DataFrame
df = pd.read_csv("Premium Collection Audit - Sheet1.csv", sep=";")

# Display the first 5 rows
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Print the column names and their data types
print(df.info())

import altair as alt

# Filter out rows with null values in any of the columns.
filtered_df = df.dropna()

# Calculate and print descriptive statistics of `Total Premium`
print("The descriptive statistics of the Total Premium are as follows:")
print(
    filtered_df["Total Premium"]
    .describe()
    .to_markdown(numalign="left", stralign="left")
)

# Plot a histogram of `Total Premium`

chart = (
    alt.Chart(filtered_df)
    .mark_bar()
    .encode(
        alt.X("Total Premium:Q", bin=True, title="Total Premium"),
        alt.Y("count()", title="Count of Policies"),
        tooltip=[alt.Tooltip("Total Premium:Q", bin=True), "count()"],
    )
    .properties(title="Distribution of Total Premium")
)

chart.save("total_premium_histogram.json")

import json

# Cargar el gráfico desde el archivo JSON
with open("total_premium_histogram.json", "r") as f:
    chart_json = json.load(f)
# Mostrar el gráfico utilizando Altair
altair_chart = alt.Chart.from_dict(chart_json)
altair_chart
