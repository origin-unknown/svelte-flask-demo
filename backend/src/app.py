from flask import Flask
import random

app = Flask(__name__, 
    static_url_path='', 
)

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/api/rand')
def api_rand():
	return str(random.randint(0, 100))
