import pandas as pd

# File paths
file1 = "downfilter.csv"
file2 = "upfilter.csv"
output_file = "totalDEGs.csv"

# Reading the CSV files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Combining the files
combined_df = pd.concat([df1, df2], ignore_index=True)

# Saving the combined file
combined_df.to_csv(output_file, index=False)

print(f"Combined file saved to: {output_file}")

# import csv

# file_path = "merged_file_with_gene_symbol - Copy.csv"
# output_path = "merged_file_with_gene_symbol - Copy1.csv"

# # Open the CSV file and read/write data
# row_number = 419  # Specify the 0-based index of the row to update
# value_to_fill = "1"

# # Read the CSV file
# with open(file_path, mode='r') as file:
#     reader = csv.reader(file)
#     rows = list(reader)

# # Debugging output
# print(f"Total number of rows: {len(rows)}")

# # Ensure the row exists
# if row_number < len(rows):
#     rows[row_number] = [value_to_fill] * len(rows[row_number])
# else:
#     print(f"Row {row_number} does not exist. Creating a new row.")
#     new_row = [value_to_fill] * (len(rows[0]) if rows else 1)  # Match existing row length or default to 1 column
#     rows.append(new_row)

# # Write back to a new CSV file
# with open(output_path, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(rows)

# print("Row updated successfully!")