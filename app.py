from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health():
	return jsonify({'result': 'ok'})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='80', debug=True)
