from flask import request, url_for, render_template, send_file, redirect

import utils
from app import app
from objects.base import UrlObject
from rpc.rpc_client import TaskClient

task_rpc = TaskClient()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/<name>', methods=['GET'])
def image(name):
    if name == 'logo.png':
        return send_file('logo.png')
    elif name == 'time':
        time = utils.time()
        return render_template('time.html', time=time)
    else:
        # Call RPC server
        record = UrlObject(short_link=name)
        origin_link = task_rpc.query_database(record)
    return redirect(origin_link.get('org_link'))


@app.route('/', methods=['POST'])
def accept():
    data_request = request.form['org_link']
    rand_link = utils.rand()
    record = UrlObject(org_link=data_request, short_link=rand_link)
    # Call RPC server
    task_rpc.insert_database(record)
    url = url_for('home', _external=True)
    final_url = url + rand_link
    return render_template('output.html', url=final_url)
