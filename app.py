from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/hello-world-<int:number>', methods=['GET'])
def hello_world(number):
    response = {
        'message': 'Hello World {number}'
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
