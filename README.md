📂 Dataset

For this assignment, I used the Iris dataset from sklearn.datasets.

It contains measurements of iris flowers with the following columns:

sepal length (cm)

sepal width (cm)

petal length (cm)

petal width (cm)

target (species: 0 = Setosa, 1 = Versicolor, 2 = Virginica)

📝 Steps Performed
1. Load & Explore the Dataset

Loaded the Iris dataset into a pandas DataFrame.

Displayed first rows with .head().

Checked data structure with .info().

Verified missing values with .isnull().sum().

2. Basic Data Analysis

Generated descriptive statistics with .describe().

Grouped by species (target) and computed mean values.

3. Data Visualizations

Created 4 plots to visualize the dataset:

Line Chart – Sepal length trend for first 30 samples.

Bar Chart – Average sepal length per species.

Histogram – Distribution of sepal width.

Scatter Plot – Relationship between sepal length and petal length.

📊 Findings & Observations

Species differ significantly in petal length and sepal length.

Setosa flowers generally have shorter petals compared to Virginica.

Sepal width is more spread out across species.

Scatter plots show clear separation between some species (e.g., Setosa vs Virginica).

⚙️ How to Run

Clone this repository:

git clone https://github.com/NeoMarvin/data-analysis-assignment.git
cd data-analysis-assignment


Install dependencies (if not already installed):

pip install pandas matplotlib seaborn scikit-learn


Run the script:

python data_analysis.py


Or open data_analysis.ipynb in Jupyter Notebook and run each cell.

✅ Requirements

Python 3.8+

pandas

matplotlib

seaborn

scikit-learn
