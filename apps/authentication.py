import argparse

from flask import Flask, request, jsonify

from controller.user_controller import UserController

app = Flask(__name__)

@app.route('/generate_user', methods=['POST'])
def generate_user():
    nik = request.form.get('nik')
    role = request.form.get('role')
    if nik is None or role is None:
        return jsonify({'error': 'parameters NIK and role are required'}),500
    elif len(nik) < 16:
        return jsonify({'error': 'Invalid NIK, length of NIK must be 16'}),500
    else:
        user = UserController()
        data, status = user.generate_user(nik=nik, role=role)
        return jsonify(data), status

@app.route('/login', methods=['POST'])
def login():
    nik = request.form.get('nik')
    password = request.form.get('password')
    if nik is None or password is None:
        return jsonify({'error': 'parameters NIK and password are required'}),500
    elif len(nik) < 16:
        return jsonify({'error': 'Invalid NIK, length of NIK must be 16'}),500
    else:
        user = UserController()
        data, status = user.authenticate(nik, password)
        return jsonify(data), status

@app.route('/userdata', methods=['GET','POST'])
def userdata():
    nik = request.form.get('nik')
    jwt = request.form.get('jwt')
    user = UserController()
    data, status = user.display_user(nik=nik, jwt=jwt)
    return jsonify(data), status

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="custom port")
    parser.add_argument('--port', type=int, default=5000, help='Port number to run the server on')
    args = parser.parse_args()

    app.run(host="0.0.0.0", port=args.port, debug=True)
