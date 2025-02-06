import pandas as pd
import numpy as np
from sklearn.preprocessing import quantile_transform
import os

# Step 1: Specify the input and output file paths
input_file = 'GSE43176_series_matrix.txt'  # Replace with your dataset
output_file = 'GSE43176_log_quantile_normalized_data.csv'

# Step 2: Check if the input file exists
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Input file '{input_file}' not found. Please check the path.")

# Step 3: Read the microarray dataset from the .txt file
microarray_data = pd.read_csv(input_file, sep='\t')

# Ensure the "ID_REF" column exists
if "ID_REF" not in microarray_data.columns:
    raise ValueError("'ID_REF' column not found in the dataset. Ensure the dataset has this column.")

# Set the "ID_REF" column as the index
microarray_data.set_index("ID_REF", inplace=True)

# Step 4: Handle non-positive values before log2 transformation
if (microarray_data <= 0).any().any():
    print("Warning: Dataset contains non-positive values. Adding a small constant (1e-5) to the data.")
    microarray_data += 1e-5  # Make all values strictly positive

# Apply log2 transformation
log2_transformed_data = np.log2(microarray_data)

# Step 5: Perform quantile normalization on the log2-transformed data
quantile_normalized_data = quantile_transform(
    log2_transformed_data, 
    n_quantiles=min(50, log2_transformed_data.shape[0]),  # Adjust n_quantiles to data size
    axis=0, 
    random_state=0, 
    copy=True
)

# Step 6: Convert the normalized data back to a DataFrame
quantile_normalized_data = pd.DataFrame(
    quantile_normalized_data, 
    columns=microarray_data.columns, 
    index=microarray_data.index
)

# Step 7: Write the normalized data to a new CSV file
quantile_normalized_data.to_csv(output_file)

print(f"Normalized data has been saved to '{output_file}'")
