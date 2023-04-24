from flask import Flask, render_template, url_for, json

app = Flask(__name__)


def get_data():
    with open('data.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        return data['SERVICES'], data['CONTACTS']


SERVICES, CONTACTS = get_data()


@app.route('/')
def index():
    context = {
        'services': SERVICES
    }
    return render_template('pages/index.html', context=context)


@app.route('/services/<string:name>')
def service(name):
    context = SERVICES[name]
    context['url_for'] = url_for('static', filename=f'images/services/{name}.jpg')
    return render_template('pages/service.html', context=context)


@app.route('/contacts')
def contacts():
    context = {
        'address': CONTACTS['address'],
        'phone': CONTACTS['phone'],
        'email': CONTACTS['email']
    }
    return render_template('pages/contacts.html', context=context)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
