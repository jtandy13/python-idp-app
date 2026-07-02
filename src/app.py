from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)

@app.route('/')

def health_check():
    return {"status": "healthy"}, 200

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': socket.gethostname(),
        'message': 'This is the details page!!'
    })

@app.route('/api/v1/healthz')

def healthz():
    return jsonify({'status': 'up'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')


# '/api/v1/details'
# '/api/v1/healthz'