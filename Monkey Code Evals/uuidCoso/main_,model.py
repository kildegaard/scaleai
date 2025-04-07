import pandas as pd
import uuid


def fix_database_values(customers_df, stores_df, sales_df):
    """Fixes common empty values in customer, store, and sales dataframes.

    Args:
        customers_df: Pandas DataFrame containing customer data.
        stores_df: Pandas DataFrame containing store data.
        sales_df: Pandas DataFrame containing sales data.

    Returns:
        Tuple of fixed dataframes: (customers_df, stores_df, sales_df)
    """

    def fix_customers(customers_df, sales_df):
        # Generate UUIDs for missing customer IDs
        customers_df["customer_id"] = customers_df["customer_id"].apply(
            lambda x: str(uuid.uuid4()) if pd.isna(x) else x
        )

        # Replace None with empty strings in name columns
        customers_df[["customer_first_name", "customer_last_name"]] = customers_df[
            ["customer_first_name", "customer_last_name"]
        ].fillna("")

        # Calculate total spent from sales data
        total_spent = sales_df.groupby("customer_id")["total_amount"].sum()
        customers_df["total_spent"] = (
            customers_df["customer_id"].map(total_spent).fillna(0)
        )

        # Find most frequented store for each customer
        most_frequented_store = sales_df.groupby("customer_id")["store_id"].agg(
            lambda x: x.value_counts().index[0]
        )
        customers_df["customer_main_store"] = customers_df["customer_id"].map(
            most_frequented_store
        )

        return customers_df

    def fix_stores(stores_df):
        # Generate UUIDs for missing store IDs
        stores_df["store_id"] = stores_df["store_id"].apply(
            lambda x: str(uuid.uuid4()) if pd.isna(x) else x
        )

        # Set store status to "CLOSED" if staff is missing
        stores_df.loc[stores_df["store_staff"].isna(), "store_status"] = "CLOSED"

        # Set store status to "OPENED" if staff exists but status is "CLOSED"
        stores_df.loc[
            (stores_df["store_staff"].notna())
            & (stores_df["store_status"] == "CLOSED"),
            "store_status",
        ] = "OPENED"

        return stores_df

    def fix_sales(sales_df):
        # Generate UUIDs for missing sales IDs
        sales_df["sales_id"] = sales_df["sales_id"].apply(
            lambda x: str(uuid.uuid4()) if pd.isna(x) else x
        )

        return sales_df

    # Fix each dataframe
    customers_df = fix_customers(customers_df.copy(), sales_df.copy())
    stores_df = fix_stores(stores_df.copy())
    sales_df = fix_sales(sales_df.copy())

    return customers_df, stores_df, sales_df


# Example dataframes (with some missing values)
customers_data = {
    "customer_id": [None, "c2", "c3"],
    "customer_first_name": ["Alice", None, "Charlie"],
    "customer_last_name": ["Smith", "Johnson", "Brown"],
    "customer_birth_date": ["1990-01-01", "1985-05-15", "1998-12-20"],
    "customer_main_store": [None, "s2", None],
    "total_spent": [None, None, None],
}

stores_data = {
    "store_id": ["s1", None, "s3"],
    "store_city": ["New York", "Los Angeles", "Chicago"],
    "store_postal_code": ["10001", "90001", "60601"],
    "store_staff": [10, None, 5],
    "store_status": ["OPENED", "CLOSED", "OPENED"],
}

sales_data = {
    "sales_id": [None, "sa2", "sa3"],
    "customer_id": ["c1", "c1", "c3"],
    "store_id": ["s1", "s2", "s1"],
    "total_amount": [100.50, 50.25, 75.00],
}

customers_df = pd.DataFrame(customers_data)
stores_df = pd.DataFrame(stores_data)
sales_df = pd.DataFrame(sales_data)

# Fix the dataframes
fixed_customers_df, fixed_stores_df, fixed_sales_df = fix_database_values(
    customers_df, stores_df, sales_df
)

print(fixed_customers_df)
print(fixed_stores_df)
print(fixed_sales_df)
