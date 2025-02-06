# import pandas as pd

# # Step 1: Load both CSV files
# file1 = "GSE43176_log_quantile_normalized_data.csv"  # Replace with your first file name
# file2 = "totalDegs.csv"    # Replace with your second file name

# # Read the files into pandas DataFrames
# df1 = pd.read_csv(file1)
# df2 = pd.read_csv(file2)

# # Step 2: Ensure 'ID_REF' column exists in both files
# if "ID_REF" not in df1.columns or "ID_REF" not in df2.columns:
#     raise ValueError("'ID_REF' column missing in one or both files.")

# # Step 3: Merge the files based on 'ID_REF'
# merged_df = pd.merge(df1, df2, on="ID_REF", how="inner")  # Inner join: keeps only matching IDs

# # Step 4: Save the merged file to a new CSV file
# merged_df.to_csv("merged_file.csv", index=False)

# print("Files have been merged and saved as 'merged_file.csv'.")
import pandas as pd

# Step 1: Load both CSV files
series_matrix_file = "GSE43176_log_quantile_normalized_data.csv"  # Replace with your Series Matrix file name
deg_file = "totalDegs.csv"                # Replace with your DEG file name

# Read the files into pandas DataFrames
series_matrix = pd.read_csv(series_matrix_file)
deg_data = pd.read_csv(deg_file)

# Step 2: Ensure 'ID_REF' column exists in both files
if "ID_REF" not in series_matrix.columns or "ID_REF" not in deg_data.columns:
    raise ValueError("'ID_REF' column missing in one or both files.")

# Step 3: Merge the files based on 'ID_REF'
merged_df = pd.merge(series_matrix, deg_data, on="ID_REF", how="inner")  # Inner join: keeps only matching IDs

# Step 4: Move 'Gene Symbol' to the first column
if "Gene.symbol" in merged_df.columns:
    # Rearrange columns: 'Gene Symbol' first, then the rest
    cols = ["Gene.symbol"] + [col for col in merged_df.columns if col != "Gene.symbol"]
    merged_df = merged_df[cols]
else:
    print("Warning: 'Gene Symbol' column not found in the merged data.")

# Step 5: Save the merged file to a new CSV file
merged_df.to_csv("merged_file_with_gene_symbol.csv", index=False)

print("Files have been merged and saved as 'merged_file_with_gene_symbol.csv'.")

