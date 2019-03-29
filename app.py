from flask import Flask, request, jsonify
from models.hoge import hoge

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health():
	hoge.v = 2
	return jsonify({'result': f'v: {hoge.v}, ok: {id(request.url)}'})


@app.route('/slow', methods=['GET'])
def slow():
	from time import sleep

	hoge.v = 1
	sleep(10)
	return jsonify({'result': f'v: {hoge.v}, slow: {id(request.url)}'})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port='80', debug=True)
