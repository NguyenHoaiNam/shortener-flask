import utils
from app import app
from app.openstack import connect
from app.openstack import network
from flask import request, url_for, render_template, send_file, redirect
from models import db, Url

session = db.session
conn = connect.create_connection(
    auth_url='http://192.168.100.41:5000/identity/v3',
    region='RegionOne',
    project_name='admin',
    username='admin',
    password='abc123',
    user_domain_id='default',
    project_domain_id='default'
)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/logo.png', methods=['GET'])
def image():
    return send_file('logo.png')


@app.route('/time', methods=['GET'])
def time():
    time_now = utils.time()
    return render_template('time.html', time=time_now)


@app.route('/<short_link>', methods=['GET'])
def main_feature(short_link):
    try:
        org_link = Url.query.filter_by(short_link=short_link).first()
    except Exception:
        raise Exception
    if org_link is None:
        return render_template('not_link.html')
    return redirect(org_link.org_link)


@app.route('/openstack/<action>', methods=['GET'])
def action_openstack(action):
    if action == 'list_net':
        list_name_net = []
        list_net = network.list_networks(conn)
        for net in list_net:
            list_name_net.append(net.name)
        return list_name_net


@app.route('/', methods=['POST'])
def accept():
    data_request = request.form['org_link']
    rand_link = utils.rand()
    record = Url(org_link=data_request, short_link=rand_link)
    try:
        session.add(record)
        session.commit()
    except Exception as e:
        raise e
    url = url_for('home', _external=True)
    final_url = url + rand_link
    return render_template('output.html', url=final_url)
