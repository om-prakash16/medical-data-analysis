# Medical-data-analysis
Medical Data Analysis
This code analyzes a medical dataset (in a CSV file named "medical_records.csv").

Libraries used:

pandas (for data manipulation)
matplotlib.pyplot (for plotting charts)
seaborn (for creating informative visualizations)
What this code does:

Reads the data: Reads the medical data from "medical_records.csv".
Explores the data:
Prints the first few rows to get an idea of the data.
Shows the column names (features).
Provides summary statistics of the data, including both numerical and categorical data types.
Analyzes Stroke data:
Filters data for patients diagnosed with Stroke.
Summarizes the Stroke data with descriptive statistics.
Groups data by Disease:
Groups data by disease category and calculates summary statistics.
Creates visualizations (uncomment the option that works for your Seaborn version):
Creates a boxplot to see the distribution of Age across different Disease Categories.
Creates a violin plot (similar to a boxplot but shows more data distribution details) of Age by Disease Category.
Note:

You might need to update the seaborn library to use the showmeans argument in the boxplot and violin plot options.
Further Exploration:

This code provides a basic analysis of the data. You can modify it to explore other features, create different visualizations (like scatter plots), or answer specific questions about the data.
