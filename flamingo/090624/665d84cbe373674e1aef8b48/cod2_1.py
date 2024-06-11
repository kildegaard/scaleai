import psycopg2
import psycopg2.extras
import json


def search_patient_records(name=None, age_range=None, medication=None, lab_result=None):
    # Database connection settings
    DB_HOST = "localhost"
    DB_PORT = 5432
    DB_NAME = "patient_database"
    DB_USER = "patient_user"
    DB_PASSWORD = "patient_password"

    # Establish a connection to the database
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )

    # Open a cursor to perform database operations
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # Construct the SQL query based on the search criteria
    query = "SELECT * FROM patients WHERE 1=1 "
    params = ()

    if name:
        query += "AND name ILIKE %s "
        params += ("%" + name + "%",)

    if age_range:
        query += "AND age BETWEEN %s AND %s "
        params += (age_range[0], age_range[1])

    if medication:
        query += "AND medications ILIKE %s "
        params += ("%" + medication + "%",)

    if lab_result:
        query += "AND lab_results ILIKE %s "
        params += ("%" + lab_result + "%",)

    # Execute the query and fetch the results
    cur.execute(query, params)
    results = cur.fetchall()

    # Convert the results to JSON
    patient_records = []
    for row in results:
        patient_record = {
            "id": row["id"],
            "name": row["name"],
            "age": row["age"],
            "medical_history": row["medical_history"],
            "medications": row["medications"],
            "lab_results": row["lab_results"],
        }
        patient_records.append(patient_record)

    # Close the cursor and connection
    cur.close()
    conn.close()

    # Return the patient records in JSON format
    return json.dumps(patient_records)


records = search_patient_records(
    name="John Doe", age_range=(30, 50), medication="Aspirin"
)
print(records)
