from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/hello-world-2', methods=['GET'])
def hello_world_2():
    response = {
        'message': 'Hello World 2'
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
