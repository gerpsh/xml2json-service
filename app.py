from flask import Flask, request
import xmltodict
import json
app = Flask(__name__)

@app.route('/', methods=['POST'])
def convert():
    resp = app.response_class(
        response=json.dumps(xmltodict.parse(request.data)),
        status=200,
        mimetype='application/json'
    )
    return resp

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
