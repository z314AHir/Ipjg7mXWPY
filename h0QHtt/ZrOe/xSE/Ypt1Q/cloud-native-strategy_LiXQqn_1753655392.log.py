from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/message')
def get_message():
    return jsonify({"message": "Hello from the cloud-native backend!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
