import pandas as pd
from sklearn.feature_selection import mutual_info_classif

# Read the transposed dataset (ensure the file path is correct)
data = pd.read_csv('transposed_file.csv')

# Ensure all features are numeric (except the last column, which is the class)
data.iloc[:, :-1] = data.iloc[:, :-1].apply(pd.to_numeric, errors='coerce')

# Convert the class label (last column) to a numeric value
data['Class'] = data['Class'].astype('category').cat.codes

# Separate features and target
X = data.iloc[:, :-1]  # All columns except the last one (features)
y = data['Class']      # Last column as target (class)

# Calculate mutual information for all features
mi_scores = mutual_info_classif(X, y)

# Create a DataFrame to store features and their scores
mi_scores_df = pd.DataFrame({
    'Feature': X.columns,
    'Score': mi_scores
}).sort_values(by='Score', ascending=False)

# Select the top 300 features based on scores
top_features = mi_scores_df.head(300)['Feature'].tolist()

# Subset the original dataset for the selected features and include the class label
selected_data = data[top_features + ['Class']]

# Save the selected features and class label to a CSV file
selected_data.to_csv('selected_features_with_class.csv', index=False)

# Save features with their scores to another CSV file
mi_scores_df.head(300).to_csv('selected_300_features_with_scores.csv', index=False)

# Confirm that the files have been saved
print("Selected features and their expression values with class label saved to 'selected_features_with_class.csv'.")
print("Selected features and their scores saved to 'selected_300_features_with_scores.csv'.")
