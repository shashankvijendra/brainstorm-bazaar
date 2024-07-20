import pandas as pd

# Load data from a CSV file
df = pd.read_csv('/home/shashank/Downloads/Electric_Vehicle_Population_Data.csv')

# Assuming 'column_name' is the name of the column you're interested in
# Replace 'column_name' with the actual column name from your dataset

# Calculate and print mean
mean_value = df['Postal Code'].mean()
print(f'Mean: {mean_value}')

# Calculate and print median
median_value = df['Model Year'].median()
print(f'Median: {median_value}')

# Calculate and print mode(s)
mode_values = df['Legislative District'].mode()
print(f'Mode(s): {mode_values}')

# Calculate and print standard deviation
std_dev = df['Model Year'].std()
print(f'Standard Deviation: {std_dev}')

# Calculate and print variance
variance = df['Electric_Range'].var()
print(f'Variance: {variance}')

# Query based on the requirement
df.query("Electric_Range>202 and City in ['Everett', 'Renton']")

#Usage of the mask which replaces the values 
df['Electric_Range'] = df['Electric_Range'].mask(df['Electric_Range'] > 336, 340)
