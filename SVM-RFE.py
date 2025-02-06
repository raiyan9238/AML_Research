import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Read the dataset (use the selected features file)
data = pd.read_csv("selected_features_with_class.csv")

# Separate features (X) and target (y)
X = data.iloc[:, :-1]  # All columns except the last one are features
y = data['Class']  # The last column is the class label

# Convert to numeric if not already
X = X.apply(pd.to_numeric)
y = y.astype('category').cat.codes

# SVM-RFE function with visualization
def svm_rfe_plot(X, y, num_features_to_select):
    # Initialize variables
    remaining_features = list(X.columns)
    ranking = []
    num_features_remaining = []
    min_weights = []
    
    while len(remaining_features) > num_features_to_select:
        # Train SVM with linear kernel
        svc = SVC(kernel="linear", C=1.0)
        svc.fit(X[remaining_features], y)
        
        # Compute feature weights (absolute values of the coefficients)
        weights = np.abs(svc.coef_).flatten()
        
        # Identify the least important feature
        least_important_feature = remaining_features[np.argmin(weights)]
        
        # Remove the least important feature
        remaining_features.remove(least_important_feature)
        
        # Update the ranking and tracking variables
        ranking.append(least_important_feature)
        num_features_remaining.append(len(remaining_features))
        min_weights.append(np.min(weights))
    
    # Add remaining features to the ranking
    ranking.extend(remaining_features)
    
    # Plot the feature elimination process
    plt.figure(figsize=(10, 6))
    plt.plot(num_features_remaining, min_weights, marker="o", color="blue")
    plt.xlabel("Number of Features Remaining")
    plt.ylabel("Minimum Feature Importance (Weight)")
    plt.title("SVM-RFE Feature Elimination")
    plt.grid()
    plt.show()
    
    # Return the top features
    top_features = ranking[-num_features_to_select:]
    return top_features

# Number of features to select
num_features_to_select = 200  # Change this to your desired number of features

# Apply SVM-RFE and visualize
selected_features = svm_rfe_plot(X, y, num_features_to_select)

# Extract the selected features along with the class label
selected_data = data[selected_features + ['Class']]

# Save the selected features to a CSV file
selected_data.to_csv("svm_rfe_selected_features.csv", index=False)

print("Selected features saved to 'svm_rfe_selected_features.csv'.")
