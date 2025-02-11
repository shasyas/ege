from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Б'
    return render_template('index.html',name=name)

app.run(host='0.0.0.0', port=5000,debug=True)