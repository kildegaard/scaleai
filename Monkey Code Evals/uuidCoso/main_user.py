import pandas as pd
import uuid


def fix_empty_values(customers_df, stores_df, sales_df):
    """Fixes common empty values in customer, store, and sales dataframes.

    Args:
        customers_df: Pandas DataFrame containing customer data.
        stores_df: Pandas DataFrame containing store data.
        sales_df: Pandas DataFrame containing sales data.

    Returns:
        Tuple of fixed dataframes: (customers_df, stores_df, sales_df)
    """

    # --- Sales Table Fixes ---
    def fix_sales(df):
        # Replace missing IDs with UUIDs
        df["sales_id"] = df["sales_id"].apply(
            lambda x: str(uuid.uuid4()) if pd.isna(x) else x
        )
        return df

    # --- Stores Table Fixes ---
    def fix_stores(df):
        # Replace missing IDs with UUIDs
        df["store_id"] = df["store_id"].apply(
            lambda x: str(uuid.uuid4()) if pd.isna(x) else x
        )

        # Set store_status to "CLOSED" if store_staff is missing and set it to "OPENED" if store_staff is not missing
        df["store_status"] = df.apply(
            lambda row: "CLOSED" if pd.isna(row["store_staff"]) else "OPENED", axis=1
        )

        # Set store_staff to zero if store_staff is missing
        df["store_staff"] = df.apply(
            lambda row: 0 if pd.isna(row["store_staff"]) else row["store_staff"], axis=1
        )

        return df

    # --- Customers Table Fixes ---
    def fix_customers(df):
        # Replace missing IDs with UUIDs
        df["customer_id"] = df["customer_id"].apply(
            lambda x: str(uuid.uuid4()) if pd.isna(x) else x
        )

        # Replace None with empty strings in name columns
        df[["customer_first_name", "customer_last_name"]] = df[
            ["customer_first_name", "customer_last_name"]
        ].fillna("")

        # Calculate total_spent from sales data
        total_spent = (
            sales_df.groupby("customer_id")["total_amount"].sum().reset_index()
        )
        df = df.merge(total_spent, on="customer_id", how="left")
        df["total_spent"] = df["total_spent"].fillna(df["total_amount"])
        df["total_spent"] = df["total_spent"].fillna(
            0
        )  # in case there are no sales for a customer
        df.drop(columns=["total_amount"], inplace=True)

        # Find most frequented store for missing customer_main_store
        most_frequented_store = (
            sales_df.groupby("customer_id")["store_id"]
            .agg(lambda x: pd.Series.mode(x)[0])
            .reset_index()
        )
        df = df.merge(most_frequented_store, on="customer_id", how="left")
        df["customer_main_store"] = df["customer_main_store"].fillna(df["store_id"])
        df.drop(columns=["store_id"], inplace=True)

        return df

    # Apply fixes to each dataframe
    sales_df = fix_sales(sales_df.copy())
    stores_df = fix_stores(stores_df.copy())
    customers_df = fix_customers(customers_df.copy())

    return customers_df, stores_df, sales_df


# Create example dataframes (replace with your actual data)
customers_data = {
    "customer_id": [
        None,
        "c03e305d-6c63-434a-947d-48e48e633c9c",
        "ecd1574a-05a7-4fdb-9ef9-f009134a70b1",
    ],
    "customer_first_name": ["Alice", None, "Charlie"],
    "customer_last_name": ["Smith", "Johnson", None],
    "customer_birth_data": ["1990-01-01", "1985-05-15", "1998-12-20"],
    "customer_main_store": [None, "14c6a822-4546-40b0-8541-dab49e82712d", None],
    "total_spent": [None, None, None],
}

stores_data = {
    "store_id": [
        None,
        "14c6a822-4546-40b0-8541-dab49e82712d",
        "8ce8b23f-40e2-4d0b-ad4f-90f66730f118",
    ],
    "store_city": ["New York", "Los Angeles", "Chicago"],
    "store_postal_code": ["10001", "90001", "60601"],
    "store_staff": [None, 10, 5],
    "store_status": [None, "OPENED", "CLOSED"],
}

sales_data = {
    "sales_id": [
        None,
        "1a33f3b7-2e9d-4838-93af-753a163a6450",
        "ea32a616-b6ab-442c-a23c-4a6a622a6566",
    ],
    "customer_id": [
        "c03e305d-6c63-434a-947d-48e48e633c9c",
        "c03e305d-6c63-434a-947d-48e48e633c9c",
        "ecd1574a-05a7-4fdb-9ef9-f009134a70b1",
    ],
    "total_amount": [100.50, 50.25, 75.00],
    "store_id": [
        "14c6a822-4546-40b0-8541-dab49e82712d",
        "8ce8b23f-40e2-4d0b-ad4f-90f66730f118",
        "14c6a822-4546-40b0-8541-dab49e82712d",
    ],
}

customers_df = pd.DataFrame(customers_data)
stores_df = pd.DataFrame(stores_data)
sales_df = pd.DataFrame(sales_data)

# Fix empty values
fixed_customers_df, fixed_stores_df, fixed_sales_df = fix_empty_values(
    customers_df, stores_df, sales_df
)

print(fixed_customers_df)
print(fixed_stores_df)
print(fixed_sales_df)
