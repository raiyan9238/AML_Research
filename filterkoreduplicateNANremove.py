import pandas as pd

# Load the CSV file
input_file = 'up.csv'  # Replace with your file name
output_file = 'upfilter.csv'  # Name for the output file

# Read the CSV into a DataFrame
df = pd.read_csv(input_file)
df = df.dropna(subset=['Gene.symbol'])
# Remove duplicates, keeping the row with the minimum p.value for each Gene.symbol
filtered_df = df.loc[df.groupby('Gene.symbol')['P.Value'].idxmin()]

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv(output_file, index=False)

print(f"Filtered data saved to {output_file}")
