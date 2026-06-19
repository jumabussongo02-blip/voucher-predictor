from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    code = generate_code(data['length'], data['special'])
    return json.dumps({"code": code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
