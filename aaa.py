from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')

@app.route('/getbannersdata')
def getbannersdata():
    return {'aaa'}

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')