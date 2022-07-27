from flask import Flask, render_template
import os


app = Flask(__name__)

def stress():

    time_in_seconds = 420

    cmd = f"stress --cpu 1 --timeout {time_in_seconds}s"

    os.system(cmd)

    return 0

@app.route('/')
def start():

    return render_template('index.html')

@app.route('/ping')
def ping():

    result = {
        "ping"  : "pong"
    }
    return result

@app.route('/stress')
def stress():
    
    stress()

if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)

    