from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "A8c-E2g-B1d-W8f+123_MySQL",  # Ensure this matches your MySQL password
    "database": "bopcus_db"
}

# Function to connect to MySQL
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

# API Route: Search BOPCUS Categories
@app.route('/search', methods=['GET'])
def search_bopcus():
    search_term = request.args.get('query', '').strip()

    if not search_term:
        return jsonify({"error": "Please provide a search query"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT category_code, description, required_documents 
        FROM bopcus_categories
        WHERE category_code LIKE %s OR description LIKE %s
        """
        cursor.execute(query, (f"%{search_term}%", f"%{search_term}%"))
        results = cursor.fetchall()

        cursor.close()
        conn.close()

        if results:
            return jsonify(results)
        else:
            return jsonify({"message": "No matching records found"}), 404

    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {err}"}), 500

# Run Flask API
if __name__ == '__main__':
    app.run(debug=True, port=5000)
