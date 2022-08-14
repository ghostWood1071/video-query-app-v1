import json
from click import command

from flask import Flask, render_template
from flask import request
from DbHelper import *
import pyodbc

app = Flask(__name__)
app.template_folder = "./"
app.static_folder = "./"
connection = pyodbc.connect(connect_str)


@app.route('/send-segments', methods=['POST'])
def send_segments():
    data = request.get_json()
    segments = list()
    for key in data:
        segments.append(data[key])
    json_data = json.dumps(segments)
    create_video_seg(connection, json_data)
    print("segments: ", data)
    return request.get_json()


@app.route('/send-sequences', methods=['POST'])
def send_sequences():
    data = request.get_json()
    print("sequences: ", data)
    json_data = json.dumps(data)
    create_frame_seq(connection, json_data)
    res = {'data': data}
    return res


@app.route('/send-frames', methods=['POST'])
def send_frames():
    data = request.get_json()
    print("frames: ", data)
    json_data = json.dumps(data)
    create_frame(connection, json_data)
    res = {'data': data}
    return res


@app.route('/send-people', methods=['POST'])
def send_people():
    data = request.get_json()
    print("people: ", data)
    if len(data) > 0:
        json_data = json.dumps(data)
        create_person(connection, json_data)
    res = {'data': data}
    return res


@app.route('/send-things', methods=['POST'])
def send_things():
    data = request.get_json()
    print("things: ", data)
    if len(data) > 0:
        json_data = json.dumps(data)
        create_things(connection, json_data)
    res = {'data': data}
    return res

@app.route('/query', methods=['POST'])
def query():
    command = request.get_data().decode("utf-8")
    result = ex_query(connection, command)
    res = json.dumps(result)
    return res

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='192.168.248.1', port=1071, debug=True)
