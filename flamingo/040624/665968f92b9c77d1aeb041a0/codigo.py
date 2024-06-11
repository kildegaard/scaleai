from flask import Flask, request, jsonify

app = Flask(__name__)


def register_user(username, email, password):
    """
    Register a new user.
    Parameters:
    username (str): The username of the new user.
    email (str): The email address of the new user.
    password (str): The password of the new user.
    Returns:
    dict: A dictionary containing a success message if registration is successful,
    or an error message if registration fails.
    """
    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # Check if email is already registered
    # Dummy implementation, replace with actual database check
    if email == "existing@email.com":
        return jsonify({"error": "Email already registered"}), 400

    # Dummy implementation, always return success
    return jsonify({"message": "User registered successfully"}), 200


@app.route("/register", methods=["POST"])
def handle_registration():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    return register_user(username, email, password)


if __name__ == "__main__":
    app.run(debug=True)
