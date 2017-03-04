import utils
from app import app
from flask import request, url_for, render_template, send_file, redirect
from models import db, Url

session = db.session


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/<name>', methods=['GET'])
def image(name):
    if name == 'logo.png':
        return send_file(name)
    elif name == 'time':
        time = utils.time()
        return render_template('time.html', time=time)
    else:
        try:
            org_link = Url.query.filter_by(short_link=name).first()
        except Exception:
            raise Exception
        if org_link is None:
            return render_template('not_link.html')
        return redirect(org_link.org_link)


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
