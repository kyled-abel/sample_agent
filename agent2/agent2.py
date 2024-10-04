from flask import Flask, request

app = Flask(__name__)

@app.route('/multiplication')
def hello_world():
    operation = request.headers.get('operation')

    output = str(eval(operation))
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)