import json
from flask import Flask, request, jsonify
from flask_cors import CORS

# Read the JSON file
with open('data.json', 'r') as file:
    marks_data = json.load(file)

# Convert the list to a dictionary for easier lookup
marks_dict = {entry['name']: entry['marks'] for entry in marks_data}

# Create Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    
    # Find marks for given names
    result_marks = []
    for name in names:
        mark = marks_dict.get(name)
        if mark is not None:
            result_marks.append(mark)
    
    return jsonify({"marks": result_marks})
