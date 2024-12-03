import pandas as pd
import numpy as np

#Set 3

#Comman Question

# Load the dataset
file_path = "D:\Downloads\AQI_Data.csv"
data = pd.read_csv(file_path)

# Display the first 5 rows
print("\nFirst 5 rows of the dataset:\n")
print(data.head(5))

# Display the last 6 rows
print("\nLast 6 rows of the dataset:\n")
print(data.tail(6))

# Summary statistics of all numeric columns
print("\nSummary statistics of numeric columns:\n ")
print(data.describe())


#Set 3 Question

# using numpy to compute the mean AQI,PM2.5,PM10
cities_mean = data.groupby('City')[['AQI', 'PM2.5', 'PM10']].agg(np.mean)

print("\nMean AQI, PM2.5, and PM10 for each city using NumPy:")
print(cities_mean)
print()

#filter and display all rows where the PM2.5 level exceeds 100(unhealthy levels) and Count how many such rows exists in each city.

unhealthy_levels = data[data['PM2.5'] > 100]  # Filter rows where PM2.5 > 100


cities_count = {}

for city in unhealthy_levels['City']:
    cities_count[city] = cities_count.get(city, 0) + 1

# Display the rows where PM2.5  exceeds 100
print("\nRows where PM2.5 exceeds 100 (Unhealthy levels):")
print(unhealthy_levels)

# Display the count of such rows for each city
print("\nCount of such rows for each city:")
for city, count in cities_count.items():
    print(f"{city}: {count}")
