import pandas as pd

# Main function to generate upregulated and downregulated DEG files
def generate_deg_files(input_file, upregulated_file, downregulated_file):
    # Load the CSV file
    data = pd.read_csv(input_file)
    
    # Filter for Upregulated DEGs: adj.P.Val < 0.05 and logFC > 1
    upregulated_deg = data[(data['adj.P.Val'] < 0.05) & (data['logFC'] > 1)]
    
    # Filter for Downregulated DEGs: adj.P.Val < 0.05 and logFC < -1
    downregulated_deg = data[(data['adj.P.Val'] < 0.05) & (data['logFC'] < -1)]
    
    # Save the filtered dataframes to CSV files
    upregulated_deg.to_csv(upregulated_file, index=False)
    downregulated_deg.to_csv(downregulated_file, index=False)

    print(f"Upregulated DEG file saved to: {upregulated_file}")
    print(f"Downregulated DEG file saved to: {downregulated_file}")

# Input and output file paths
input_file = "GSE43176.top.table.csv"  # Replace with the path to your main CSV file
upregulated_file = "up.csv"  # Replace with your desired output path
downregulated_file = "down.csv"  # Replace with your desired output path

# Generate DEG files
generate_deg_files(input_file, upregulated_file, downregulated_file)
