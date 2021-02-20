import json
import mechanicalsoup


from flask import Flask
from markupsafe import escape

app = Flask(__name__)


def login_municipality_rionegro(user: str, password: str) -> dict:
    url = 'http://entidadesintegradas.co/Registro/faces/Index?60N5MP1O=1'
    url_login_ok = 'http://entidadesintegradas.co/Registro/faces/Main.xhtml'

    try:
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(url=url)
        browser.select_form()

        # fill-in the form
        browser['login:_t61'] = user
        browser['login:j_idt65'] = password
        browser.new_control(type='input',
                            name='javax.faces.source',
                            value='login:btnLogin')
        browser.new_control(type='input',
                            name='javax.faces.partial.event',
                            value='click')
        browser.new_control(type='input',
                            name='javax.faces.partial.execute',
                            value='login:btnLogin login:btnLogin')
        browser.new_control(type='input',
                            name='javax.faces.partial.render',
                            value='login')
        browser.new_control(type='input',
                            name='javax.faces.behavior.event',
                            value='click')
        browser.new_control(type='input',
                            name='javax.faces.partial.ajax',
                            value='true')

        browser.submit_selected()
    except Exception as error:
        return {
            'status': 'fail',
            'response': str(error)
        }

    return {
        'status': 'success' if browser.url == url_login_ok else 'fail',
        'response': str(browser.page)
    }


def create_account_municipality_rionegro() -> str:
    url = 'http://entidadesintegradas.co/Registro/faces/Index?60N5MP1O=1'
    url_create_account = 'http://entidadesintegradas.co/Registro/faces/CrearCuenta.xhtml'

    try:
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(url=url)
        browser.open(url=url_create_account)

        browser.select_form()

        # Fill-in the form
        browser['crearCuenta:_t50'] = '1'
        browser['crearCuenta:_t61'] = '1098707951'
        browser['crearCuenta:_t65'] = '123456'
        browser['crearCuenta:_t69'] = '123456'
        browser['crearCuenta:_t73'] = 'Daniel Mauricio'
        browser['crearCuenta:_t74'] = 'Sandoval'
        browser['crearCuenta:_t75'] = 'Vargas'
        browser['crearCuenta:_t79'] = 'M'
        browser['crearCuenta:_t86'] = 'derhks@gmail.com'
        browser['crearCuenta:_t90'] = '60000000'
        browser['crearCuenta:_t94'] = '3000000000'
        browser['crearCuenta:_t98'] = '5'
        browser['crearCuenta:direccion'] = 'CL 46 # 52 - 77'
        browser['crearCuenta:_t110'] = '02'
        browser['crearCuenta:_t143'] = '02'
        browser['crearCuenta:_t157'] = '1987'
        browser['crearCuenta:_t163'] = None
        browser['crearCuenta:_t167'] = 'rojo'
        browser['crearCuenta:_t171'] = None
        browser['crearCuenta:_t175'] = 'bogota'
        browser['crearCuenta:_t177'] = 'on'

        browser.submit_selected()
    except Exception as error:
        return str(error)

    return 'Success'


def mainpage_municipality_rionegro() -> str:
    try:
        url = 'http://entidadesintegradas.co/Registro/faces/Index?60N5MP1O=1'
        browser = mechanicalsoup.StatefulBrowser()
        browser.open(url=url)
    except Exception as error:
        return str(error)

    return str(browser.page)


@app.route('/', methods=['GET'])
def main_page():
    response = mainpage_municipality_rionegro()

    return {
        'statusCode': 200 if response == 'Success' else 500,
        'body': json.dumps(response)
    }


@app.route('/create_account', methods=['POST'])
def create_account():
    response = create_account_municipality_rionegro()

    return {
        'statusCode': 200 if response == 'Success' else 500,
        'body': json.dumps(response)
    }


@app.route('/login/<string:cc>/<string:password>', methods=['POST'])
def login(cc: str, password: str) -> dict:
    user = escape(cc)
    password = escape(password)
    response = login_municipality_rionegro(user=user, password=password)

    return {
        'statusCode': 200 if response['status'] == 'success' else 401,
        'body': json.dumps(response['response'])
    }
