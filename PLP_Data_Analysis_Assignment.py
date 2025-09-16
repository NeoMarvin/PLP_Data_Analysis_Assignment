# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load the Iris dataset
try:
    iris = load_iris(as_frame=True)
    df = iris.frame  
    print("Dataset loaded successfully.")
except Exception as e:
    print("Error Loading dataset:", e)

# display the first five rows
print(df.head())

# Display basic information about the dataset
print(df.info()) 

# Display  the missing values
print(df.isnull().sum())

# Display statistics summary
print(df.describe())

# Display group by species
print(df.groupby("target").mean())

# Visualizations
# Line Chart (using first 30 rows to show trend of sepal length)
df.head(30)["sepal length (cm)"].plot(kind="line", title="Line Chart: Sepal Length (First 30 samples)")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

# Bar Chart (average sepal length per species)
df.groupby("target")["sepal length (cm)"].mean().plot(kind="bar", title="Average Sepal Length per Species")
plt.xlabel("Species (0=Setosa,1=Versicolor,2=Virginica)")
plt.ylabel("Sepal Length (cm)")
plt.show()

# Histogram (distribution of sepal width)
df["sepal width (cm)"].plot(kind="hist", bins=10, title="Histogram: Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.show()

# Scatter Plot (relationship between sepal length & petal length)
df.plot(kind="scatter", x="sepal length (cm)", y="petal length (cm)", title="Scatter: Sepal vs Petal Length")
plt.show()