from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

data_file = os.path.join(os.path.dirname(__file__), 'data.json')

@app.route('/records', methods=['GET'])
def get_records():
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify([]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/records', methods=['POST'])
def add_record():
    new_record = request.json.get('record') 
    if not new_record:
        return jsonify({'error': 'No record provided'}), 400 

    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    data.append(new_record)
    try:
        with open(data_file, 'w') as file:
            json.dump(data, file)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Record added successfully'}), 201

@app.route('/records', methods=['DELETE'])
def delete_records():
    try:
        with open(data_file, 'w') as file:
            json.dump([], file)
        return jsonify({'message': 'All records deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
