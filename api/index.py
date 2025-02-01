import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load the data from the JSON file
with open('data.json', 'r') as f:
    students_data = json.load(f)

# Create the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api', methods=['GET'])
def get_student_marks():
    # Get names from query parameters
    names = request.args.getlist('name')
    
    # Fetch marks for the given names
    marks = [
        next((student["marks"] for student in students_data if student["name"] == name), None)
        for name in names
    ]

    # Return JSON response
    return jsonify({"marks": marks})

# This is for local testing
if __name__ == '__main__':
    app.run(debug=True)
