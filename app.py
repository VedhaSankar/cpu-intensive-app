from flask import Flask, render_template
import os
from multiprocessing import Pool
from multiprocessing import cpu_count
import signal

stop_loop = 0


app = Flask(__name__)

def exit_chld(x, y):

    global stop_loop
    stop_loop = 1

def f(x):

    global stop_loop
    while not stop_loop:
        x*x

# def stress():

#     time_in_seconds = 420

#     cmd = f"stress --cpu 1 --timeout {time_in_seconds}s"

#     os.system(cmd)

#     return 0

@app.route('/')
def start():

    return render_template('index.html')

@app.route('/ping')
def ping():

    result = {
        "ping"  : "pong"
    }
    return result

@app.route('/stress-cpu')
def stress_cpu():

    processes = cpu_count()
    print('-' * 20)
    print('Running load on CPU(s)')
    print('Utilizing %d cores' % processes)
    print('-' * 20)
    pool = Pool(processes)
    pool.map(f, range(processes))
    
    # stress()
    # pass

if __name__== "__main__":
    app.run(host="0.0.0.0", debug = True, port = 5003)

    