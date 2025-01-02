import argparse

from flask import Flask, request, jsonify

from controller.fetch_controller import FetchController

app = Flask(__name__)

@app.route('/fetch_data', methods=['GET','POST'])
def fetching_data():
    jwt = request.form.get('jwt')
    fc = FetchController()
    return jsonify(fc.fetching_data(jwt=jwt))

@app.route('/aggregate_data', methods=['GET','POST'])
def aggregate_data():
    jwt = request.form.get('jwt')
    role = request.form.get('role')
    fc = FetchController()
    return jsonify(fc.aggregate_data(jwt=jwt, role=role))

@app.route('/userdata', methods=['GET','POST'])
def userdata():
    nik = request.form.get('nik')
    jwt = request.form.get('jwt')
    fc = FetchController()
    return jsonify(fc.display_user(nik=nik, jwt=jwt))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="custom port")
    parser.add_argument('--port', type=int, default=5000, help='Port number to run the server on')
    args = parser.parse_args()

    app.run(host="0.0.0.0", port=args.port, debug=True)
