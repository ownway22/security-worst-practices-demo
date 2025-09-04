import hashlib
import sqlite3
import os
import subprocess
from flask import Flask, request

# Hard-coded secret (for secret scanners)
AWS_SECRET_ACCESS_KEY = "AKIAFAKESECRETKEY123456"
GCP_SERVICE_ACCOUNT_KEY = "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASC...FAKE...\n-----END PRIVATE KEY-----"
JWT_SIGNING_KEY = "super-insecure-hardcoded-jwt-key"

app = Flask(__name__)

# Insecure: unsafely building SQL from user input (SQL Injection)
@app.route('/user')
def get_user():
    username = request.args.get('name', '')
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE users (name text, password text)')
    c.execute("INSERT INTO users VALUES ('admin','secret')")
    # Vulnerable line
    query = f"SELECT * FROM users WHERE name = '{username}'"  # no sanitization
    try:
        for row in c.execute(query):
            return {'user': row[0], 'password_hash': hashlib.md5(row[1].encode()).hexdigest()}  # weak hash (MD5)
    except Exception as e:
        return {'error': str(e)}, 400

# Insecure command execution (Command Injection)
@app.route('/ping')
def ping():
    target = request.args.get('target', '127.0.0.1')
    cmd = f"ping -c 1 {target}"  # unsanitized
    output = subprocess.getoutput(cmd)
    return {'output': output}

# Weak password hashing example
@app.route('/hash')
def weak_hash():
    password = request.args.get('p', 'password123')
    return {'md5': hashlib.md5(password.encode()).hexdigest()}

if __name__ == '__main__':
    # Debug mode with host exposure
    app.run(host='0.0.0.0', port=5000, debug=True)
