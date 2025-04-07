import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv("Ints.csv")

# Calculate the sum of the integrals
df["Sum"] = df["BB"] + df["GB"] + df["RB"]

# Calculate the percentage of each band relative to the sum
df["BB_perc"] = df["BB"] / df["Sum"] * 100
df["GB_perc"] = df["GB"] / df["Sum"] * 100
df["RB_perc"] = df["RB"] / df["Sum"] * 100

# Create the figure and axes
fig, ax1 = plt.subplots()

# Plot the sum of the integrals as a function of temperature
(line1,) = ax1.plot(df["Temp"], df["Sum"], "ko-", label="Sum")
ax1.set_xlabel("Temperature (°C)")
ax1.set_ylabel("Sum of Integrals (a.u.)")
ax1.tick_params(axis="y")
ax1.ticklabel_format(axis="y", style="sci", scilimits=(4, 4))
ax1.yaxis.set_major_locator(plt.MultipleLocator(10000))

# Create a second y-axis
ax2 = ax1.twinx()

# Plot the percentage of each band relative to the sum
(line2,) = ax2.plot(df["Temp"], df["BB_perc"], "bo:", label="Blue Band")
(line3,) = ax2.plot(df["Temp"], df["GB_perc"], "rs:", label="Green Band")
(line4,) = ax2.plot(df["Temp"], df["RB_perc"], "g^:", label="Red Band")
ax2.set_ylabel("Percentage of Total Integral (%)")

# Combine the legends from both axes
lines = [line1, line2, line3, line4]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc="center")

# Show the plot
plt.show()
