from flask import request, url_for, render_template, send_file, redirect
from sqlalchemy.orm import sessionmaker, exc

import utils
from app import app
from db_create import engine
from models import Url
from rpc.rpc_client import TaskClient

#task_rpc = TaskClient()


Session = sessionmaker(bind=engine)
session = Session()


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
        #origin_link = task_rpc.query_database(session, name)
        origin_link = session.query(Url).filter(Url.short_link == name).one()
        origin_link_aaa = origin_link.org_link
    return redirect(origin_link_aaa)


@app.route('/', methods=['POST'])
def accept():
    data_request = request.form['org_link']
    rand_link = utils.rand()
    record = Url(org_link=data_request, short_link=rand_link)
    try:
        session.query(Url).filter(Url.short_link == rand_link).one()
        rand_link = utils.rand()
        record = Url(org_link=data_request, short_link=rand_link)
    except exc.NoResultFound:
        # task_rpc.insert_database(session, record)
        try:
            session.add(record)
            session.commit()
        except Exception:
            session.rollback()
            raise Exception

    url = url_for('home', _external=True)
    final_url = url + rand_link
    return render_template('output.html', url=final_url)
