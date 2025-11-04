from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('features_dataframe.csv', index_col= 0)

correlation_matrix = df.iloc[:, :-1].corr()

plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.savefig("correlation_matrix.png")


#Results: Between Maas and UniqueWordRatio keep one and between YuleK and AverageCoRoLaWordFrequency keep one


df = df.drop(['Maas', 'YuleK'], axis=1)

new_correlation_matrix = df.iloc[:, :-1].corr()

plt.figure(figsize=(10,8))
sns.heatmap(new_correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.savefig("new_correlation_matrix.png")

#label encoding for the 5 classes

labels = df.iloc[:,-1]

le = LabelEncoder()

labels_encoded = le.fit_transform(labels)

print(labels_encoded)
print(le.classes_)


df["Model"] = labels_encoded

df.to_csv("processed_features_dataframe.csv", sep = ",")