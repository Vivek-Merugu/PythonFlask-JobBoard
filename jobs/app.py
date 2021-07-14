#import route as route
from flask import render_template,Flask
app = Flask(__name__)

@app.route('/jobs')
@app.route('/')
def jobs():
    return render_template('index.html')