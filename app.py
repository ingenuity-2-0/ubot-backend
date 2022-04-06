from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from chat import get_response

app = Flask(__name__)
CORS(app)

# @app.get('/')
# def index_get():
#     return render_template('base.html')


@app.route('/chat/<string:text>')
def predict(text):
    # text = request.get_json().get('message')
    print(text)
    response = get_response(text)
    message = [{'conversation': response}]
    return jsonify(message)
    # return response


if __name__ == '__main__':
    # app.run(debug=True, host='192.168.84.134', port='8080')
    app.run(debug=True)
