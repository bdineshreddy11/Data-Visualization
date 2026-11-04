# 🚕 Data Visualization Using Python

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas">
  <img src="https://img.shields.io/badge/NumPy-Numerical_Computing-013243?style=for-the-badge&logo=numpy">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge">
  <img src="https://img.shields.io/badge/Seaborn-Statistical_Charts-4c72b0?style=for-the-badge">
</p>

<p align="center">
  <b>Exploratory Data Analysis and Visualization of New York City Taxi Trips</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Visualizations-11-blueviolet?style=flat-square">
  <img src="https://img.shields.io/badge/Dataset-Taxis-orange?style=flat-square">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=flat-square">
</p>

---

<h2 align="center">📌 Project Overview</h2>

This project focuses on exploring and visualizing New York City taxi trip data using Python. The Seaborn built-in Taxis dataset is used to understand trip patterns, fare distribution, payment methods, passenger tips, and relationships between different trip variables.

Pandas and NumPy are used for data handling and cleaning, while Matplotlib and Seaborn are used to create different types of visualizations. The project includes missing value handling, data exploration, date conversion, and 11 different charts to present the findings clearly.

<h2 align="center">🎯 Project Objectives</h2>

<table>
<tr>
<td width="50%" valign="top">

<h3>🔵 Data Analysis</h3>

- Explore the dataset structure.
- Understand numerical and categorical columns.
- Analyze taxi fares and trip distances.
- Identify payment and trip patterns.

</td>
<td width="50%" valign="top">

<h3>🟣 Data Visualization</h3>

- Create different chart types.
- Compare trip information.
- Understand data distributions.
- Identify relationships and correlations.

</td>
</tr>
</table>

---

<h2 align="center">🛠️ Technology Stack</h2>

<table>
<tr>
<th align="center">Technology</th>
<th align="center">Purpose</th>
<th align="center">Skills Used</th>
</tr>
<tr>
<td>🐍 Python</td>
<td>Programming language</td>
<td>Variables, loops, conditions, imports</td>
</tr>
<tr>
<td>🐼 Pandas</td>
<td>Data manipulation</td>
<td>DataFrames, filtering, grouping, cleaning</td>
</tr>
<tr>
<td>🔢 NumPy</td>
<td>Numerical operations</td>
<td>Numerical data types and operations</td>
</tr>
<tr>
<td>📊 Matplotlib</td>
<td>Basic visualization</td>
<td>Histogram, line, bar and pie charts</td>
</tr>
<tr>
<td>🎨 Seaborn</td>
<td>Statistical visualization</td>
<td>Box, count, scatter, heatmap, pair and violin plots</td>
</tr>
</table>

<h2 align="center">📂 Dataset Information</h2>

<table>
<tr>
<td width="35%" bgcolor="#E8F1FF"><b>Dataset Name</b></td>
<td>Taxis</td>
</tr>
<tr>
<td bgcolor="#E8F1FF"><b>Data Source</b></td>
<td>Seaborn Built-in Dataset</td>
</tr>
<tr>
<td bgcolor="#E8F1FF"><b>Domain</b></td>
<td>Transportation and Travel Analytics</td>
</tr>
<tr>
<td bgcolor="#E8F1FF"><b>Records</b></td>
<td>6,433</td>
</tr>
<tr>
<td bgcolor="#E8F1FF"><b>Columns</b></td>
<td>14</td>
</tr>
<tr>
<td bgcolor="#E8F1FF"><b>Data Type</b></td>
<td>Structured Data</td>
</tr>
</table>

**Dataset Loading**

```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("taxis")
```

### Dataset Columns

| Column | Description |
|:---|:---|
| `pickup` | Pickup date and time |
| `dropoff` | Drop-off date and time |
| `passengers` | Number of passengers |
| `distance` | Trip distance in miles |
| `fare` | Base trip fare |
| `tip` | Tip amount |
| `tolls` | Toll charges |
| `total` | Total trip amount |
| `color` | Taxi color |
| `payment` | Payment method |
| `pickup_zone` | Pickup location zone |
| `dropoff_zone` | Drop-off location zone |
| `pickup_borough` | Pickup borough |
| `dropoff_borough` | Drop-off borough |

---

<h2 align="center">🔄 Project Workflow</h2>

<p align="center">
  <b>Dataset Loading</b><br>
  ⬇️<br>
  <b>Data Exploration</b><br>
  ⬇️<br>
  <b>Missing Value Analysis</b><br>
  ⬇️<br>
  <b>Data Cleaning and Imputation</b><br>
  ⬇️<br>
  <b>Date Conversion</b><br>
  ⬇️<br>
  <b>Exploratory Data Analysis</b><br>
  ⬇️<br>
  <b>Matplotlib Visualizations</b><br>
  ⬇️<br>
  <b>Seaborn Visualizations</b><br>
  ⬇️<br>
  <b>Final Results</b>
</p>

---

<h2 align="center">🧹 Data Cleaning and Preprocessing</h2>

Data cleaning is performed to identify and handle missing values before visualization.

**1. Missing Value Identification**

```python
print(df.isnull().sum())
```

**2. Separating Numerical and Categorical Columns**

```python
numerical_columns = df.select_dtypes(include=np.number).columns

category_columns = df.select_dtypes(
    include=["object", "category"]
).columns
```

**3. Numerical Missing Value Imputation**

Median is used to fill missing values in numerical columns.

```python
for col in numerical_columns:
    df[col] = df[col].fillna(df[col].median())
```

**4. Categorical Missing Value Imputation**

Mode is used to fill missing values in categorical columns.

```python
for col in category_columns:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])
```

**5. Removing Remaining Missing Values**

```python
df = df.dropna()
```

**6. Date Conversion**

```python
df["pickup"] = pd.to_datetime(
    df["pickup"],
    errors="coerce"
)

df.dropna(subset=["pickup"], inplace=True)
```

---

<h2 align="center">📊 Data Visualizations</h2>

<p align="center">
  <b>11 Charts | Matplotlib + Seaborn</b>
</p>

<h3 align="center">🔵 Matplotlib Visualizations</h3>

<table>
<tr>
<td align="center" width="50%">
<h4>01. Histogram – Distribution of Tips</h4>
<img src="./outputs/Figure_1.png" width="100%" alt="Tip Distribution">
<p>Displays the frequency distribution of taxi tip amounts.</p>
</td>
<td align="center" width="50%">
<h4>02. Line Chart – Fare Over Time</h4>
<img src="outputs/figure-2.png" width="100%" alt="Fare Over Time">
<p>Shows how taxi fares change across pickup timestamps.</p>
</td>
</tr>
<tr>
<td align="center">
<h4>03. Bar Chart – Total Fare by Pickup Borough</h4>
<img src="outputs/figure-3.png" width="100%" alt="Total Fare by Borough">
<p>Compares total fare amounts across pickup boroughs.</p>
</td>
<td align="center">
<h4>04. Pie Chart – Payment Method Distribution</h4>
<img src="outputs/figure-4.png" width="100%" alt="Payment Method Distribution">
<p>Displays the percentage distribution of payment methods.</p>
</td>
</tr>
<tr>
<td align="center">
<h4>05. Histogram – Distribution of Distance</h4>
<img src="outputs/figure-5.png" width="100%" alt="Distance Distribution">
<p>Shows the frequency distribution of trip distances.</p>
</td>
<td align="center" valign="middle">
<h4>📈 Matplotlib Summary</h4>
<p><b>5 Visualizations</b></p>
<p>Histogram · Line · Bar · Pie</p>
</td>
</tr>
</table>

<h3 align="center">🟣 Seaborn Visualizations</h3>

<table>
<tr>
<td align="center" width="50%">
<h4>06. Box Plot – Tip by Pickup Borough</h4>
<img src="outputs/figure-6.png" width="100%" alt="Tip by Pickup Borough">
<p>Compares tip distributions and identifies outliers.</p>
</td>
<td align="center" width="50%">
<h4>07. Count Plot – Number of Trips by Borough</h4>
<img src="outputs/figure-7.png" width="100%" alt="Trips by Borough">
<p>Displays the number of trips in each pickup borough.</p>
</td>
</tr>
<tr>
<td align="center">
<h4>08. Scatter Plot – Fare vs Distance</h4>
<img src="outputs/figure-8.png" width="100%" alt="Fare vs Distance">
<p>Explores the relationship between trip distance and fare.</p>
</td>
<td align="center">
<h4>09. Heatmap – Correlation Matrix</h4>
<img src="outputs/figure-9.png" width="100%" alt="Correlation Matrix">
<p>Displays correlations between numerical trip variables.</p>
</td>
</tr>
<tr>
<td align="center">
<h4>10. Pair Plot – Pairwise Relationships</h4>
<img src="outputs/figure-10.png" width="100%" alt="Pair Plot">
<p>Compares relationships between distance, fare, tip and total.</p>
</td>
<td align="center">
<h4>11. Violin Plot – Fare by Payment Method</h4>
<img src="outputs/figure-11.png" width="100%" alt="Violin Plot">
<p>Compares fare distributions across payment methods.</p>
</td>
</tr>
</table>

---

<h2 align="center">📚 Skills and Topics Covered</h2>

<table>
<tr>
<th width="30%">Category</th>
<th>Skills and Topics</th>
</tr>
<tr>
<td bgcolor="#DCEBFF"><b>Python Fundamentals</b></td>
<td>Variables, imports, loops, conditional statements, comments, functions and output display</td>
</tr>
<tr>
<td bgcolor="#DDF5E4"><b>Pandas</b></td>
<td>DataFrames, dataset loading, head(), info(), describe(), shape, columns, select_dtypes(), isnull(), sum(), fillna(), dropna(), median(), mode(), groupby(), value_counts(), corr(), sample(), to_datetime()</td>
</tr>
<tr>
<td bgcolor="#F1E4FF"><b>NumPy</b></td>
<td>Numerical data types, numerical operations and integration with Pandas</td>
</tr>
<tr>
<td bgcolor="#FFE9D9"><b>Matplotlib</b></td>
<td>Histogram, line chart, bar chart, pie chart, figure size, title, labels, ticks, legends and layout adjustments</td>
</tr>
<tr>
<td bgcolor="#FFF4CC"><b>Seaborn</b></td>
<td>Box plot, count plot, scatter plot, heatmap, pair plot, violin plot and color palettes</td>
</tr>
<tr>
<td bgcolor="#E8E5FF"><b>Data Analysis</b></td>
<td>Data exploration, data cleaning, missing value handling, median and mode imputation, distribution analysis, correlation analysis, outlier detection and relationship analysis</td>
</tr>
</table>

<h2 align="center">📁 Project Structure</h2>

```text
Data-Visualization/
│
├── data.py
│
├── outputs/
│   ├── figure-1.png
│   ├── figure-2.png
│   ├── figure-3.png
│   ├── figure-4.png
│   ├── figure-5.png
│   ├── figure-6.png
│   ├── figure-7.png
│   ├── figure-8.png
│   ├── figure-9.png
│   ├── figure-10.png
│   └── figure-11.png
│
└── README.md
```

<h2 align="center">⚙️ Installation and Execution</h2>

**Step 1 – Install Required Libraries**

```bash
pip install pandas numpy matplotlib seaborn
```

**Step 2 – Clone the Repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 3 – Open the Project Folder**

```bash
cd Data-Visualization
```

**Step 4 – Run the Python Program**

```bash
python data.py
```

---

<h2 align="center">📌 Final Project Summary</h2>

<table>
<tr>
<th align="left">Project Details</th>
<th align="left">Results</th>
</tr>
<tr>
<td>Dataset</td>
<td>Taxis</td>
</tr>
<tr>
<td>Dataset Records</td>
<td>6,433 (original dataset)</td>
</tr>
<tr>
<td>Dataset Columns</td>
<td>14</td>
</tr>
<tr>
<td>Data Cleaning</td>
<td>Completed</td>
</tr>
<tr>
<td>Missing Value Check</td>
<td>Completed</td>
</tr>
<tr>
<td>Matplotlib Charts</td>
<td>5</td>
</tr>
<tr>
<td>Seaborn Charts</td>
<td>6</td>
</tr>
<tr>
<td><b>Total Visualizations</b></td>
<td><b>11</b></td>
</tr>
</table>

<h2 align="center">💡 Key Learning Outcomes</h2>

- Learned to explore and understand structured datasets.
- Practiced missing value identification and imputation.
- Improved knowledge of Pandas and NumPy.
- Created different visualizations using Matplotlib and Seaborn.
- Understood data distributions, correlations and relationships.
- Gained practical experience in exploratory data analysis.

<h2 align="center">🚀 Future Improvements</h2>

- Add more detailed exploratory data analysis.
- Explore additional taxi trip patterns.
- Create interactive visualizations using Plotly.
- Develop an interactive dashboard using Power BI.

---

<p align="center">
  <b>📊 Turning Raw Data into Meaningful Visual Insights</b>
  <br><br>
  Built with ❤️ using Python, Pandas, NumPy, Matplotlib and Seaborn.
</p>
