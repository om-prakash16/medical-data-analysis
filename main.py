import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the medical data from the CSV file
data = pd.read_csv("medical_records.csv")

# Get a quick glimpse at the first few rows of the data
print("First few rows:")
print(data.head())

# Show the column names (features) present in the data
print("\nColumn names:")
print(data.columns)

# Get some summary statistics of the data, including numerical and categorical data
print("\nSummary statistics:")
print(data.describe(include='all'))  # Include categorical data

# Filter data for patients with Stroke diagnosis
stroke_data = data[data['Disease_Category'] == 'Stroke']

# Print a summary of the Stroke data
print("\nStroke data summary:")
print(stroke_data.describe(include='all'))

# Group data by disease category and calculate statistics
disease_stats = data.groupby('Disease_Category').describe(include='all')
print("Statistics by Disease Category:")
print(disease_stats)

# **Choose the option that works for your Seaborn version (update Seaborn or remove showmeans):**

# Option 1: Update Seaborn (if possible) and use showmeans (requires Seaborn >= 0.11.0)
# sns.boxplot(
#     x = "Disease_Category",
#     y = "Age",
#     showmeans=True,
#     data=data
# )
# plt.title('Distribution of Age by Disease Category')
# plt.xlabel('Disease Category')
# plt.ylabel('Age')
# plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# plt.show()

# Option 2: Remove showmeans argument (if update is not possible)
sns.boxplot(
    x = "Disease_Category",
    y = "Age",
    # showmeans=True,  # Remove this line if you can't update Seaborn
    data=data
)
plt.title('Distribution of Age by Disease Category')
plt.xlabel('Disease Category')
plt.ylabel('Age')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# Option 1: Update Seaborn (if possible) and use showmeans (requires Seaborn >= 0.11.0)
# sns.violinplot(
#     x = "Disease_Category",
#     y = "Age",
#     showmeans=True,
#     data=data
# )
# plt.title('Distribution of Age by Disease Category (Violin Plot)')
# plt.xlabel('Disease Category')
# plt.ylabel('Age')
# plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
# plt.show()

# Option 2: Remove showmeans argument (if update is not possible)
sns.violinplot(
    x = "Disease_Category",
    y = "Age",
    # showmeans=True,  # Remove this line if you can't update Seaborn
    data=data
)
plt.title('Distribution of Age by Disease Category (Violin Plot)')
plt.xlabel('Disease Category')
plt.ylabel('Age')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()

# You can create similar plots for other numerical features and explore other data visualization techniques based on your needs.
