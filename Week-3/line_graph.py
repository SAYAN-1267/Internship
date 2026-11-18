
import matplotlib.pyplot as plt

# Sample data
days = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 200, 250]

# Plot line graph
plt.plot(days, sales, marker='o', color='blue', 
         linestyle='-', label='Daily Sales')

# Add title and labels
plt.title("Daily Sales Report")
plt.xlabel("Days")
plt.ylabel("Sales")

# Display grid and legend
plt.grid(True)
plt.legend()

# Display graph
plt.show()
