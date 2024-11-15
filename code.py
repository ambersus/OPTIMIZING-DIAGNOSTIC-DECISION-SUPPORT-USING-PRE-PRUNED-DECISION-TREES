# -*- coding: utf-8 -*-
"""Fai_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1S3FrWmhDiutkiLFy1lVxclgLnI5kaGdj
"""

# Importing necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Load the dataset (replace the path with the actual path to your CSV file)
df = pd.read_csv('/content/dataset.csv')

# Encode categorical features (like Blood Cholesterol, Blood Pressure, and Outcome)
label_encoder = LabelEncoder()

# Encoding 'Blood Pressure' column (values like 'Low', 'Normal', 'High')
df['Blood Pressure'] = label_encoder.fit_transform(df['Blood Pressure'])

# Encoding 'Cholesterol Level' column (values like 'Low', 'Normal', 'High')
df['Cholesterol Level'] = label_encoder.fit_transform(df['Cholesterol Level'])

# Encoding 'Outcome' column (values like 'Positive', 'Negative')
df['Outcome Variable'] = label_encoder.fit_transform(df['Outcome Variable'])

# If other columns are also categorical (e.g., 'Disease Name', 'Gender'), you should encode them similarly
df['Disease'] = label_encoder.fit_transform(df['Disease'])
df['Gender'] = label_encoder.fit_transform(df['Gender'])

# Features (X) and Target (Y)
X = df.drop(columns=['Outcome Variable'])  # Drop the Outcome column to get the features
y = df['Outcome Variable']  # Target variable: Outcome (Disease present or not)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Decision Tree Classifier with Pruning (max_depth limits the depth of the tree)
clf = DecisionTreeClassifier(max_depth=3, random_state=42)  # max_depth = 3 is a pruning technique

# Train the model
clf.fit(X_train, y_train)

# Predict on the test data
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Plot the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=X.columns, class_names=['Negative', 'Positive'], filled=True)
plt.title("Decision Tree for Disease Diagnosis")
plt.show()

# Plotting the real vs. predicted values

# Sort indices to ensure both lines are aligned (for visualization)
sorted_indices = np.argsort(np.arange(len(y_test)))

plt.figure(figsize=(10, 6))

# Plot real values (from test data)
plt.plot(sorted_indices, y_test.iloc[sorted_indices], color='blue', label='Real Values', marker='o')

# Plot predicted values (from the model)
plt.plot(sorted_indices, y_pred[sorted_indices], color='red', label='Predicted Values', linestyle='--', marker='x')

# Adding titles and labels
plt.title("Comparison of Real vs. Predicted Values")
plt.xlabel("Test Sample Index")
plt.ylabel("Outcome (0 = Negative, 1 = Positive)")
plt.legend()
plt.grid(True)
plt.show()