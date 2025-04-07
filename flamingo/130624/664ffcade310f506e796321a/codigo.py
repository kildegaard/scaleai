import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

data = {
    'ay': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'dy': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'dow': [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4],
    'customer_id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    'amount': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],
    'product_id': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012],
    'category': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B', 'C', 'A', 'B', 'C']
}
df1 = pd.DataFrame(data)

X1_features = df1[(df1['ay'] + df1['dy'] + df1['dow'] < 12)][["ay", "dy", "dow", "customer_id", "amount", "category"]]

encoder1 = OneHotEncoder(drop='first', sparse_output=False)
encoded_features1 = encoder1.fit_transform(X1_features[['ay', 'dy', 'dow']])
feature_names = encoder1.get_feature_names_out()

encoded_df = pd.DataFrame(encoded_features1, columns=feature_names)

encoded_df['is_first_half'] = X1_features['ay'].apply(lambda x: 1 if x <= 6 else 0)

scaler = StandardScaler()
encoded_df['amount'] = scaler.fit_transform(X1_features[['amount']])

encoded_df = pd.concat([encoded_df, X1_features[['customer_id', 'category']].reset_index(drop=True)], axis=1)

total_amount_per_customer = encoded_df.groupby('customer_id')['amount'].sum().reset_index()

encoder2 = OneHotEncoder(drop='first', sparse_output=False)
encoded_category = encoder2.fit_transform(X1_features[['category']])
category_feature_names = encoder2.get_feature_names_out(['category'])

encoded_category_df = pd.DataFrame(encoded_category, columns=category_feature_names)

encoded_df = pd.concat([encoded_df, encoded_category_df], axis=1)

average_amount_per_category = encoded_df.groupby('category')['amount'].mean().reset_index()

print("Encoded Features DataFrame:")
print(encoded_df)

print("\nTotal Amount Spent by Each Customer:")
print(total_amount_per_customer)

print("\nAverage Amount Spent Per Category:")
print(average_amount_per_category)