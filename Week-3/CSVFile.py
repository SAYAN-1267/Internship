
import pandas as pd

# Load CSV file
df = pd.read_csv("students.csv")

# Display first 5 records
print("First 5 Records:")
print(df.head())

# Display total rows and columns
print("\nShape of Dataset:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display dataset information
print("\nDataset Information:")
df.info()

# Generate statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Calculate average marks
print("\nAverage Marks:")
print(df["Marks"].mean())
