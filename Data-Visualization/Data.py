# 1) Loading the Taxis Dataset
import pandas as pd;
import numpy as np;
import seaborn as sns;
import matplotlib.pyplot as plt;
df = sns.load_dataset("taxis")
print("Top 10 rows of the dataset:")
print(df.head(10))
print("Dataset Info:")
print(df.info())
print(df.describe())
# 2) Handling Missing Values
print("Missing Values in the Dataset:")
print(df.isnull().sum())
# to impute the data for missing values seperate the numerical and category columns
numerical_columns = df.select_dtypes(include=np.number).columns
print(numerical_columns)
category_columns = df.select_dtypes(
    include=["object", "category"]
).columns
# Impute numerical columns using median
for col in numerical_columns:
    df[col] = df[col].fillna(df[col].median())
# Impute categorical columns using mode
for col in category_columns:
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].mode()[0])

#drop the rows with missing values
df = df.dropna()
print("\n missing values after imputation:")
print(df.isnull().sum())
# Data Visualization using Matplotlib
df['tip'].hist(bins=30, edgecolor='black')
plt.title('Distribution of Tips')
plt.xlabel('Tip Amount')
plt.ylabel('Frequency')
plt.show()
df["pickup"] = pd.to_datetime(df["pickup"], errors="coerce")
df.dropna(subset=["pickup"], inplace=True)
# Line Chart - Fare Over Time
plt.figure(figsize=(12, 6))
plt.plot(
    df["pickup"],
        df["fare"],
        color="blue",
        linewidth=1
)
plt.title("Fare Over Time", fontsize=16)
plt.xlabel("Pickup Timestamp")
plt.ylabel("Fare ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Bar Chart - Total Fare by Pickup Borough
plt.figure(figsize=(10, 6))
# Group by pickup borough and sum the fare
borough_fare = df.groupby("pickup_borough")["fare"].sum()
borough_fare.plot(
    kind="bar", 
    color="skyblue", 
    edgecolor="black"
)

plt.title("Total Fare by Pickup Borough", fontsize=16)
plt.xlabel("Pickup Borough")
plt.ylabel("Total Fare ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Pie Chart - Payment Method Distribution
plt.figure(figsize=(8, 8))
payment_counts = df["payment"].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Payment Method Distribution", fontsize=16)
plt.tight_layout()
plt.show()
#Histogram - Distribution of Distance
plt.figure(figsize=(10, 6))
plt.hist(df["distance"], bins=30, edgecolor="black")
plt.title("Distribution of Distance", fontsize=16)
plt.xlabel("Distance(miles)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Box Plot - Tip by Pickup Borough
plt.figure(figsize=(10, 6))
sns.boxplot(
    x="pickup_borough", 
    y="tip", 
    data=df, 
    palette="Set2"
)
plt.title("Tip Distribution by Pickup Borough", fontsize=16)
plt.xlabel("Pickup Borough")
plt.ylabel("Tip Amount ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# Data Visualization using Seaborn
#1.Count Plot - Number of Trips by Borough
plt.figure(figsize=(10, 6))
sns.countplot(x="pickup_borough", data=df,color="cornflowerblue")
plt.title("Number of Trips by Pickup Borough", fontsize=16)
plt.xlabel("Pickup Borough")
plt.ylabel("Number of Trips")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#2. Scatter Plot - Fare vs. Distance
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df,
                 x="distance", 
                 y="fare", hue="pickup_borough", 
                 alpha=0.6)
plt.title("Fare vs. Distance by Pickup Borough", fontsize=16)
plt.xlabel("Distance (miles)")
plt.ylabel("Fare ($)")
plt.legend(title="Pickup Borough")
plt.tight_layout()
plt.show()

#Heatmap - Correlation Matrix
plt.figure(figsize=(10, 8))
numeric_data = df[
    ["distance", "fare", "tip", "tolls", "total"]
]
correlation_matrix = numeric_data.corr()
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Correlation Matrix", fontsize=16)
plt.tight_layout()
plt.show()
#Pair Plot - Pairwise Relationships

pair_data = df[
    ["distance", "fare", "tip", "total", "pickup_zone"]
].dropna()

# Sample data for better performance
if len(pair_data) > 1000:
    pair_data = pair_data.sample(1000, random_state=42)
sns.pairplot(
    data=pair_data,
    vars=["distance", "fare", "tip", "total"],
    hue="pickup_zone",
    diag_kind="hist"
)
plt.suptitle(
    "Pairwise Relationships Between Trip Variables",
    y=1.02,
    fontsize=16
)
plt.show()

# Violin Plot - Fare by Payment Method
plt.figure(figsize=(10, 6))
sns.violinplot(
    x="payment",
    y="fare",
    data=df,
    inner="quartile",
    palette="pastel"
)
plt.title("Fare Distribution by Payment Method", fontsize=16)
plt.xlabel("Payment")
plt.ylabel("Fare ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Final Output
print("Dataset Shape:", df.shape)
print("Total Visualizations Created: 10")