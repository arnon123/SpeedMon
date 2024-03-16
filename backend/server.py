from flask import Flask, jsonify
from flask_cors import CORS

# Create a Flask app
app = Flask(__name__)
CORS(app)

# Define a sample API endpoint
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({'message': 'Hello, World!'})

# Define another API endpoint
@app.route('/api/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    # Run the app
    app.run(debug=True, ssl_context=('backend/certs/server.crt', 'backend/certs/server.key'))
