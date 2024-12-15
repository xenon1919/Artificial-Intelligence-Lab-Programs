import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.tree import plot_tree

# Load the dataset from your CSV file
csv_file_path = "data2.csv"
df = pd.read_csv(csv_file_path)

# Convert categorical variables into numerical
le = preprocessing.LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['Travel Cost ($)/km'] = le.fit_transform(df['Travel Cost ($)/km'])
df['Income Level'] = le.fit_transform(df['Income Level'])
df['Transportation mode'] = le.fit_transform(df['Transportation mode'])

# Features and target variable
features = ['Gender', 'Car ownership', 'Travel Cost ($)/km', 'Income Level']
X = df[features]
y = df['Transportation mode']

# Decision tree classifier
dtree = DecisionTreeClassifier()
dtree = dtree.fit(X, y)

# Visualize the decision tree
plt.figure(figsize=(10, 6))
plot_tree(dtree, feature_names=features, class_names=df['Transportation mode'].unique().astype(str), filled=True)
plt.show()
